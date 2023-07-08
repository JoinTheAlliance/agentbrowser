from browser import (
    browser,
    loop,
    pages,
    navigate_to,
    get_body_html,
    get_body_text,
    get_document_html,
    get_document_text,
    get_current_page_id,
    create_page,
    switch_to,
    close_page,
)
from collections import defaultdict

if __name__ == "__main__":
    # Check if the browser has been initialized
    assert browser is not None, "Browser initialization failed."

    # Check if the asyncio event loop has been set
    assert loop is not None, "Event loop initialization failed."

    # Check if the pages dictionary has been initialized correctly
    assert isinstance(pages, defaultdict), "Pages initialization failed."

    # Check if the current_page_id is None as expected initially
    assert get_current_page_id() is None, "current_page_id initialization failed."

    print("All tests passed.")

    print(get_current_page_id())

    test_page_id_1 = create_page(None)
    print("test_page_id_1")
    print(test_page_id_1)

    test_page_id_2 = create_page("https://www.google.com")
    print("test_page_id_2")
    print(test_page_id_2)

    switch_to(test_page_id_1)

    close_page(test_page_id_1)

    print("current_page_id")
    print(get_current_page_id())

    assert (
        get_current_page_id() == test_page_id_2
    ), "current_page_id is not test_page_id_2"

    # navigate to google
    navigate_to("https://www.google.com")

    # Get HTML
    html = get_document_html()
    print('*** HTML')
    print(html)

    text = get_document_text()

    # Get title
    title = browser.title()

    # Get body
    body = get_body_html()

    print('*** BODY')
    print(body)

    body_text = get_body_text()

    print('*** BODY TEXT')
    print(body_text)

    # fill out google search and press submit

    # get urls

    # get images

    # get pdfs

    # get zips

    # get videos

    # execute some pyppeteer code

    # try searching a page, crawling the links, crawling the links, and then crawling the links of the links just to make sure the bugs are gud

#    TODO: add browser history for each page