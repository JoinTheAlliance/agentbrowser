import asyncio
import pytest
from agentbrowser import (
    async_get_browser,
    async_init_browser,
    async_navigate_to,
    async_get_body_html,
    async_get_body_text,
    async_get_document_html,
    async_create_page,
    async_close_page,
    async_evaluate_javascript,
)

from agentbrowser.browser import browser, context

test_article = "https://test-page-to-crawl.vercel.app"

@pytest.mark.asyncio
async def test_async_create_page():
    global browser
    global context
    browser = None
    context = None
    await async_init_browser()
    test_page = await async_create_page("https://www.google.com/")
    assert test_page is not None, "Page navigation failed."
    assert test_page.url == "https://www.google.com/", "Navigation failed."
    print("test_create_page passed.")

    await async_close_page(test_page)
    assert test_page.is_closed(), "Page failed to close."
    print("test_close_page passed.")

    test_page = await async_create_page("https://www.google.com")

    # navigate to google
    await async_navigate_to(
        "https://www.yahoo.com",
        test_page,
    )

    assert test_page.url != "https://www.google.com", "Navigation failed."
    assert test_page is not None, "Page navigation failed."
    print("test_async_navigation passed.")

    body_html = await async_get_body_html(test_page)
    assert body_html is not None, "Failed to get body html."
    print("test_async_body_html passed.")

    html = await async_get_document_html(test_page)
    assert html is not None, "Failed to get document html."
    print("test_async_document_html passed.")

    body = await async_get_body_text(test_page)
    assert body is not None, "Failed to get body text."
    print("test_async_body_text passed.")

    result = await async_evaluate_javascript(
        """
        var x = 1;
        var y = 2;
        var z = x + y;
        z;
        """,
        test_page,
    )
    assert result == 3, "Javascript evaluation failed."
    print("test_async_javascript_evaluation passed.")
