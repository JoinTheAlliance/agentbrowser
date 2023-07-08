import asyncio
import signal
from pyppeteer import launch
from collections import defaultdict
from typing import Dict
import uuid

loop = asyncio.get_event_loop()
browser = None
pages: Dict[str, Dict] = defaultdict(dict)
current_page_id = None


def run_until_complete(future):
    loop.run_until_complete(future)


def handle_interrupt():
    asyncio.ensure_future(close_browser())
    loop.stop()


async def init_browser():
    global browser
    browser = await launch()
    signal.signal(signal.SIGINT, handle_interrupt)


loop.run_until_complete(init_browser())


async def close_browser():
    await browser.close()


async def create_page(site=None):
    global current_page_id
    page = await browser.newPage()
    page_id = str(uuid.uuid4())
    if site:
        await page.goto(site)
    pages[page_id] = page
    current_page_id = page_id
    return page_id


def get_current_page_id():
    return current_page_id


def get_current_page():
    return pages[current_page_id]


def switch_to(page_id):
    global current_page_id
    if page_id in pages:
        current_page_id = page_id
    else:
        raise ValueError(f"Page ID {page_id} does not exist.")


async def close_page(page_id=current_page_id):
    global current_page_id
    if page_id in pages:
        page = pages[page_id]
        await page.close()
        del pages[page_id]
        if current_page_id == page_id:
            if len(pages) > 0:
                next_page_id = list(pages.keys())[0]
            else:
                next_page_id = None
        current_page_id = next_page_id
    else:
        raise ValueError(f"Page ID {page_id} does not exist.")


async def navigate_to(url, page_id=current_page_id):
    if not page_id:
        page_id = await create_page(None)
        raise ValueError("No active page.")
    page = pages[page_id]
    try:
        await page.goto(url)
    except Exception as e:
        print("Error navigating to: " + url)
        print(e)
        return None
    await page.goto(url)
    return page


async def get_document_html(page_id=current_page_id):
    if not page_id:
        raise ValueError("No active page.")
    page = pages[page_id]
    return await page.content()


async def get_document_text(page_id=current_page_id):
    if not page_id:
        raise ValueError("No active page.")
    page = pages[page_id]
    return await page.Jeval("document", "(element) => element.textContent")


async def get_body_text(page_id=current_page_id):
    if not page_id:
        raise ValueError("No active page.")
    page = pages[page_id]
    return await page.Jeval("body", "(element) => element.textContent")


async def get_body_html(page_id=current_page_id):
    if not page_id:
        raise ValueError("No active page.")
    page = pages[page_id]
    return await page.Jeval("body", "(element) => element.innerHTML")


async def evaluate_javascript(code, page_id=current_page_id):
    if not page_id:
        raise ValueError("No active page.")
    else:
        page = pages[page_id]
        await page.evaluate(code)
