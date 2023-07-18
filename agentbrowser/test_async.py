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
    async_get_body_text_raw,
)
from agentbrowser.browser import get_body_text_raw

test_article = "https://test-page-to-crawl.vercel.app"


@pytest.fixture(scope="function")
async def browser_fixture(request):
    # Initialize a new event loop for this test
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Initialize the browser
    await async_init_browser()
    assert await async_get_browser() is not None, "Browser initialization failed."

    async def fin():
        # cleanup after tests
        if await async_get_browser() is not None:
            await (await async_get_browser()).close()

        loop.run_until_complete(
            asyncio.sleep(0.250)
        )  # gives tasks a bit of time to finish

    request.addfinalizer(fin)

    yield


@pytest.mark.asyncio
async def test_async_create_page(browser_fixture):
    test_page = await async_create_page("https://www.google.com/")
    assert test_page is not None, "Page navigation failed."
    assert test_page.url == "https://www.google.com/", "Navigation failed."
    print("test_create_page passed.")

    await async_close_page(test_page)
    assert test_page.isClosed(), "Page failed to close."
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

    body_text_raw = await async_get_body_text_raw(test_page)
    assert body_text_raw is not None, "Failed to get raw body text."
    print("test_async_body_text_raw passed.")

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
