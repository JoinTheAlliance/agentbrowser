import asyncio
from pyppeteer import launch
import os
import platform

browser = None


def get_browser():
    if browser is None:
        init_browser()
    return browser


async def async_get_browser():
    if browser is None:
        await async_init_browser()
    return browser


def init_browser(headless=True, executable_path=None):
    asyncio.get_event_loop().run_until_complete(
        async_init_browser(headless, executable_path)
    )


def create_page(site=None):
    return asyncio.get_event_loop().run_until_complete(async_create_page(site))


def close_page(page):
    asyncio.get_event_loop().run_until_complete(async_close_page(page))


def navigate_to(url, page):
    return asyncio.get_event_loop().run_until_complete(async_navigate_to(url, page))


def get_document_html(page):
    return asyncio.get_event_loop().run_until_complete(async_get_document_html(page))


def get_body_text(page):
    return asyncio.get_event_loop().run_until_complete(async_get_body_text(page))


def get_body_text_raw(page):
    return asyncio.get_event_loop().run_until_complete(async_get_body_text_raw(page))


def get_body_html(page):
    return asyncio.get_event_loop().run_until_complete(async_get_body_html(page))


def evaluate_javascript(code, page):
    return asyncio.get_event_loop().run_until_complete(
        async_evaluate_javascript(code, page)
    )


# async version of init_browser
async def async_init_browser(headless=True, executable_path=None):
    global browser

    if executable_path is None:
        executable_path = find_chrome()

    if browser is None:
        browser = await launch(
            headless=headless,
            executablePath=executable_path,
            autoClose=False,
            # set handleSIGINT to False to allow for graceful shutdown
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
        )
    return browser


# async version of create_page
async def async_create_page(site=None):
    global browser
    new_browser = None
    if browser is None:
        new_browser = await async_init_browser()
    else:
        new_browser = browser
    page = await new_browser.newPage()
    if site:
        await page.goto(site, {"waitUntil": ["domcontentloaded", "networkidle0"]})
    return page


# async version of close_page
async def async_close_page(page):
    await page.close()


# async version of navigate_to
async def async_navigate_to(url, page):
    if not page:
        page = await async_create_page(None)
    try:
        await page.goto(url, {"waitUntil": ["domcontentloaded", "networkidle0"]})
    except Exception as e:
        print("Error navigating to: " + url)
        print(e)
        return None
    return page


# async version of get_document_html
async def async_get_document_html(page):
    return await page.content()


async def async_get_body_text(page):
    output = await page.querySelectorEval("body", "(element) => element.innerText")
    return output.strip()


async def async_get_body_text_raw(page):
    output = await page.querySelectorEval("body", "(element) => element.innerText")
    return output.strip()


# async version of get_body_html
async def async_get_body_html(page):
    return await page.Jeval("body", "(element) => element.innerHTML")


# async version of evaluate_javascript
async def async_evaluate_javascript(code, page):
    return await page.evaluate(code)


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
