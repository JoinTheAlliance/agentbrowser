from agentbrowser import (
    create_page,
    evaluate_javascript,
    get_body_html,
    get_body_text,
    get_document_html,
    navigate_to
)
from agentbrowser.browser import close_page, get_page_title, init_browser, get_browser, screenshot_page

test_article = "https://test-page-to-crawl.vercel.app"


def test_get_browser():
    browser = get_browser()
    assert browser is not None, "Failed to get the browser"
    print("test_get_browser passed.")


def test_init_browser():
    init_browser()
    browser = get_browser()
    assert browser is not None, "Failed to initialize the browser"
    print("test_init_browser passed.")


def test_navigation():
    test_page = create_page("https://www.google.com")

    # navigate to google
    navigate_to(
        "https://www.yahoo.com",
        test_page,
        wait_until="domcontentloaded",
    )

    assert test_page.url != "https://www.google.com", "Navigation failed."
    assert test_page is not None, "Page navigation failed."
    print("test_navigation passed.")


def test_get_page_title():
    test_page = create_page("https://www.google.com")
    title = get_page_title(test_page)
    assert title == "Google", "Failed to get the correct page title."
    print("test_get_page_title passed.")


def test_screenshot_page():
    test_page = create_page("https://www.google.com")
    screenshot = screenshot_page(test_page)
    assert screenshot is not None, "Failed to take a screenshot."
    print("test_screenshot_page passed.")


def test_close_page():
    test_page = create_page("https://www.google.com")
    close_page(test_page)
    assert test_page.is_closed(), "Failed to close the page."
    print("test_close_page passed.")


def test_body_html():
    test_page = create_page(test_article)
    body_html = get_body_html(test_page)
    assert body_html is not None, "Failed to get body html."
    print("test_body_html passed.")


def test_document_html():
    test_page = create_page(test_article)
    html = get_document_html(test_page)
    assert html is not None, "Failed to get document html."
    print("test_document_html passed.")


def test_body_text():
    test_page = create_page(test_article)
    body = get_body_text(test_page)
    assert body is not None, "Failed to get body text."
    print("test_body_text passed.")


def test_javascript_evaluation():
    test_page = create_page(test_article)
    result = evaluate_javascript(
        """
        var x = 1;
        var y = 2;
        var z = x + y;
        z;
        """,
        test_page,
    )
    assert result == 3, "Javascript evaluation failed."
    print("test_javascript_evaluation passed.")
