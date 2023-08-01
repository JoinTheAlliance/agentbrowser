import asyncio
from playwright.async_api import async_playwright

import os
import platform

browser = None
context = None


def ensure_event_loop():
    """
    Ensure that there is an event loop in the current thread.

    If no event loop exists, a new one is created and set for the current thread.

    :return: The current event loop.
    :rtype: asyncio.AbstractEventLoop
    """
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop


# Synchronous functions


def get_browser():
    """
    Get a Playwright browser.

    If the browser doesn't exist, initializes a new one.

    :return: A Playwright browser.
    :rtype: playwright.async_api.Browser
    """
    ensure_event_loop()
    global browser
    if browser is None:
        init_browser()
    return browser


def init_browser(headless=True, executable_path=None):
    """
    Initialize a new Playwright browser.

    :param headless: Whether the browser should be run in headless mode, defaults to True.
    :type headless: bool, optional
    :param executable_path: Path to a Chromium or Chrome executable to run instead of the bundled Chromium.
    :type executable_path: str, optional
    """
    ensure_event_loop()
    asyncio.get_event_loop().run_until_complete(
        async_init_browser(headless, executable_path)
    )


def create_page(site=None):
    """
    Create a new page in the browser.

    If a site is provided, navigate to that site.

    :param site: URL to navigate to, defaults to None.
    :type site: str, optional
    :return: A new page.
    :rtype: playwright.async_api.Page
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_create_page(site))


def close_page(page):
    """
    Close a page.

    :param page: The page to close.
    :type page: playwright.async_api.Page
    """
    ensure_event_loop()
    asyncio.get_event_loop().run_until_complete(async_close_page(page))


def navigate_to(url, page, wait_until="domcontentloaded"):
    """
    Navigate to a URL in a page.

    :param url: The URL to navigate to.
    :type url: str
    :param page: The page to navigate in.
    :type page: playwright.async_api.Page
    :return: The page after navigation.
    :rtype: playwright.async_api.Page
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_navigate_to(url, page, wait_until=wait_until))


def get_document_html(page):
    """
    Get the HTML content of a page.

    :param page: The page to get the HTML from.
    :type page: playwright.async_api.Page
    :return: The HTML content of the page.
    :rtype: str
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_get_document_html(page))


def get_page_title(page):
    """
    Get the title of a page.

    :param page: The page to get the title from.
    :type page: playwright.async_api.Page
    :return: The title of the page.
    :rtype: str
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_get_page_title(page))


def get_body_text(page):
    """
    Get the text content of a page's body.

    :param page: The page to get the text from.
    :type page: playwright.async_api.Page
    :return: The text content of the page's body.
    :rtype: str
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_get_body_text(page))


def get_body_html(page):
    """
    Get the HTML content of a page's body.

    :param page: The page to get the HTML from.
    :type page: playwright.async_api.Page
    :return: The HTML content of the page's body.
    :rtype: str
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_get_body_html(page))


def screenshot_page(page):
    """
    Get a screenshot of a page.

    :param page: The page to screenshot.
    :type page: playwright.async_api.Page
    :return: A bytes object representing the screenshot.
    :rtype: bytes
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(async_screenshot_page(page))


def evaluate_javascript(code, page):
    """
    Evaluate JavaScript code in a page.

    :param code: The JavaScript code to evaluate.
    :type code: str
    :param page: The page to evaluate the code in.
    :type page: playwright.async_api.Page
    :return: The result of the evaluated code.
    """
    ensure_event_loop()
    return asyncio.get_event_loop().run_until_complete(
        async_evaluate_javascript(code, page)
    )


# Asynchronous functions


async def async_get_browser():
    """
    Get a Playwright browser asynchronously.

    If the browser doesn't exist, initializes a new one.

    :return: A Playwright browser.
    :rtype: playwright.async_api._generated.Browser
    """
    global browser
    if browser is None:
        await async_init_browser()
    return browser


async def async_init_browser(headless=True, executable_path=None):
    """
    Initialize a new Playwright browser asynchronously.

    :param headless: Whether the browser should be run in headless mode, defaults to True.
    :type headless: bool, optional
    :param executable_path: Path to a Chromium or Chrome executable to run instead of the bundled Chromium.
    :type executable_path: str, optional
    :return: A new Playwright browser.
    :rtype: playwright.async_api._generated.Browser
    """
    global browser

    if executable_path is None:
        executable_path = find_chrome()

    if browser is None:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=headless,
            executable_path=executable_path,
        )
    return browser


async def async_create_page(site=None):
    """
    Create a new page in the browser asynchronously.

    If a site is provided, navigate to that site.

    :param site: URL to navigate to, defaults to None.
    :type site: str, optional
    :return: A new page.
    :rtype: playwright.async_api._generated.Page
    """
    global browser
    if browser is None:
        await async_init_browser()
    context = await browser.new_context()
    page = await context.new_page()
    if site:
        await page.goto(site, wait_until="domcontentloaded")
    return page


async def async_close_page(page):
    """
    Close a page asynchronously.

    :param page: The page to close.
    :type page: playwright.async_api._generated.Page
    """
    await page.close()


async def async_navigate_to(url, page, wait_until="domcontentloaded"):
    """
    Navigate to a URL in a page asynchronously.

    :param url: The URL to navigate to.
    :type url: str
    :param page: The page to navigate in.
    :type page: playwright.async_api._generated.Page
    :return: The page after navigation.
    :rtype: playwright.async_api._generated.Page
    """
    if not page:
        page = await async_create_page(None)
    try:
        await page.goto(url, wait_until=wait_until)
    except Exception as e:
        print("Error navigating to: " + url)
        print(e)
        return None
    return page


async def async_get_document_html(page):
    """
    Get the HTML content of a page asynchronously.

    :param page: The page to get the HTML from.
    :type page: playwright.async_api._generated.Page
    :return: The HTML content of the page.
    :rtype: str
    """
    return await page.content()


async def async_get_page_title(page):
    """
    Get the title of a page asynchronously.

    :param page: The page to get the title from.
    :type page: playwright.async_api._generated.Page
    :return: The title of the page.
    :rtype: str
    """
    return await page.title()


async def async_get_body_text(page):
    """
    Get the text content of a page's body asynchronously.

    :param page: The page to get the text from.
    :type page: playwright.async_api._generated.Page
    :return: The text content of the page's body.
    :rtype: str
    """
    body_handle = await page.query_selector("body")
    return await page.evaluate("(body) => body.innerText", body_handle)


async def async_get_body_html(page):
    """
    Get the HTML content of a page's body asynchronously.

    :param page: The page to get the HTML from.
    :type page: playwright.async_api._generated.Page
    :return: The HTML content of the page's body.
    :rtype: str
    """
    body_handle = await page.query_selector("body")
    return await page.evaluate("(body) => body.innerHTML", body_handle)


async def async_screenshot_page(page):
    """
    Get a screenshot of a page asynchronously.

    :param page: The page to screenshot.
    :type page: playwright.async_api._generated.Page
    :return: A bytes object representing the screenshot.
    :rtype: bytes
    """
    return await page.screenshot()


async def async_evaluate_javascript(code, page):
    """
    Evaluate JavaScript code in a page asynchronously.

    :param code: The JavaScript code to evaluate.
    :type code: str
    :param page: The page to evaluate the code in.
    :type page: playwright.sync_api.Page
    :return: The result of the evaluated code.
    """
    return await page.evaluate(code)


def find_chrome():
    """
    Find the Chrome executable.

    :return: The path to the Chrome executable, or None if it could not be found.
    :rtype: str
    """
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
