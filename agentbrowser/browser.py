import asyncio
import re
import signal
from pyppeteer import launch
import os
import platform

browser = None


def get_browser():
    check_browser_inited()
    return browser


def init_browser(headless=True, executable_path=None):
    if browser is not None:
        asyncio.get_event_loop().run_until_complete(browser.close())

    if executable_path is None:
        executable_path = find_chrome()

    async def init():
        global browser

        def handle_interrupt():
            asyncio.ensure_future(browser.close())
            asyncio.get_event_loop().stop()

        browser = await launch(headless=headless, executablePath=executable_path)
        signal.signal(signal.SIGINT, handle_interrupt)

    asyncio.get_event_loop().run_until_complete(init())


def check_browser_inited():
    if browser is None:
        init_browser()


def create_page(site=None):
    check_browser_inited()
    page = asyncio.get_event_loop().run_until_complete(browser.newPage())
    if site:
        asyncio.get_event_loop().run_until_complete(
            page.goto(site, {"waitUntil": ["domcontentloaded", "networkidle0"]})
        )
    return page


def close_page(page):
    asyncio.get_event_loop().run_until_complete(page.close())


def navigate_to(url, page):
    check_browser_inited()
    if not page:
        page = create_page(None)
    try:
        asyncio.get_event_loop().run_until_complete(
            page.goto(url, {"waitUntil": ["domcontentloaded", "networkidle0"]})
        )
    except Exception as e:
        print("Error navigating to: " + url)
        print(e)
        return None
    return page


def get_document_html(page):
    return asyncio.get_event_loop().run_until_complete(page.content())


def get_body_text(page):
    # get the body, but remove some junk first
    output = asyncio.get_event_loop().run_until_complete(
        page.Jeval(
            "body",
            """
        (element) => {
            const element_blacklist = [
                "sidebar",
                "footer",
                "account",
                "login",
                "signup",
                "search",
                "advertisement",
                "masthead",
                "popup",
                "floater",
                "modal",
            ];
            // first, filter out all the script tags, noscript tags, <footer>, <header>, etc
            [...element.querySelectorAll('script, noscript, form, footer, header, img, svg, style')].forEach(element => element && element.remove())
            // find any element which contains any class or id which includes the words in the blacklist
            const blacklist = element_blacklist.join('|')
            const regex = new RegExp(blacklist, 'i')
            const blacklist_elements = [...element.querySelectorAll('*')].filter(element => element && ((element.id && element.id.match(regex)) || (element.className && element.className.match && element.className.match(regex))))
            // remove all the blacklist elements
            blacklist_elements.forEach(element => element && element.remove())
            // replace any tags inside of the body with just their text content
            const tags = [...element.querySelectorAll('*')]
            tags.forEach(element => element && element.replaceWith(element.textContent))

            // then, get the text content of the body element
            let text = element.textContent
            // finally, remove all the extra whitespace
            text = text.replace(/\s+/g, ' ')
            return text
        }
        """,
        )
    )

    # remove any extra whitespace
    output = re.sub(r"\s+", " ", output)

    return output


def get_body_text_raw(page):
    # get the raw body text, without any filtering
    return asyncio.get_event_loop().run_until_complete(
        page.Jeval(
            "body",
            """
        (element) => {
            return element.textContent
        }
        """,
        )
    )


def get_body_html(page):
    return asyncio.get_event_loop().run_until_complete(
        page.Jeval("body", "(element) => element.innerHTML")
    )


def evaluate_javascript(code, page):
    return asyncio.get_event_loop().run_until_complete(page.evaluate(code))


def find_chrome():
    if platform.system() == "Windows":
        paths = [
            os.path.join(
                os.environ["ProgramFiles(x86)"],
                "Google",
                "Chrome",
                "Application",
                "chrome.exe",
            ),
            os.path.join(
                os.environ["ProgramFiles"],
                "Google",
                "Chrome",
                "Application",
                "chrome.exe",
            ),
            os.path.join(
                os.environ["LocalAppData"],
                "Google",
                "Chrome",
                "Application",
                "chrome.exe",
            ),
        ]
    elif platform.system() == "Darwin":
        paths = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    elif platform.system() == "Linux":
        paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium",
            "/usr/bin/chromium-browser",
        ]
    else:
        print("Unsupported platform")
        return None

    for path in paths:
        if os.path.exists(path):
            return path

    return None
