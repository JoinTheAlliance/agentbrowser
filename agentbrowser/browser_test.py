from browser import (
    get_browser,
    init_browser,
    navigate_to,
    get_body_html,
    get_body_text,
    get_body_text_raw,
    get_document_html,
    create_page,
    close_page,
    evaluate_javascript,
)


def main():
    # Initialize the browser
    init_browser()

    # Check if the browser has been initialized
    assert get_browser() is not None, "Browser initialization failed."

    test_page = create_page("https://www.google.com")
    print("test_page")
    print(test_page)

    # navigate to google
    navigate_to(
        "https://www.lesswrong.com/posts/gEchYntjSXk9KXorK/uncontrollable-ai-as-an-existential-risk",
        test_page,
    )

    body_html = get_body_html(test_page)
    print("*** BODY HTML")
    print(body_html)

    # Get HTML
    html = get_document_html(test_page)
    print("*** HTML")
    print(html)

    # Get body
    body = get_body_text(test_page)

    print("*** BODY, test_page_2")
    print(body)

    body_text = get_body_text(test_page)

    body_text_raw = get_body_text_raw(test_page)

    print("*** BODY TEXT, test_page")
    print(body_text)

    print("*** BODY TEXT RAW, test_page")
    print(body_text_raw)

    evaluate_javascript(
        """
        var x = 1;
        var y = 2;
        var z = x + y;
        console.log(z);
        """,
        test_page,
    )

    close_page(test_page)


main()
