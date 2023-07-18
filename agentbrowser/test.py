from agentbrowser import (
    create_page,
    evaluate_javascript,
    get_body_html,
    get_body_text,
    get_document_html,
    navigate_to,
)
from agentbrowser.browser import get_body_text_raw

test_article = "https://test-page-to-crawl.vercel.app"


def test_navigation():
    test_page = create_page("https://www.google.com")

    # navigate to google
    navigate_to(
        "https://www.yahoo.com",
        test_page,
    )

    assert test_page.url != "https://www.google.com", "Navigation failed."
    assert test_page is not None, "Page navigation failed."
    print("test_navigation passed.")


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


def test_body_text_raw():
    test_page = create_page(test_article)
    body_text_raw = get_body_text_raw(test_page)
    assert body_text_raw is not None, "Failed to get raw body text."
    print("test_body_text_raw passed.")


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
