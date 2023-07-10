# agentbrowser

A browser for your agent, built on Chrome and Pyppeteer.

<img src="resources/image.jpg">

# Installation

```bash
pip install agentbrowser
```

# Usage

## Importing into your project

```python
from agentbrowser import (
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
```

# Basic:

# Create a new page

Equivalent of ctrl+t in Chrome. Makes a new blank page.

```python
page = create_page()
```

# Close a page

Equivalent of ctrl+w in Chrome. Closes the current page.

```python
close_page(page)
```

## Navigate to a URL

Equivalent of typing a URL into the address bar and hitting enter.
If you haven't created a page yet, it will create one for you.

```python
page = navigate_to("https://google.com")
```

## Get the HTML of the page

Get the entire document HTML

```python
html = get_document_html(page)
```

## Get the HTML of the body

Get just the HTML of the body and inner. Useful for parsing out the content of the page.

```python
html = get_body_html(page)
```

## Get the text of the body

Get just the text of the body. Unlike the raw function, tries to remove some useless tags and divs and things. Not perfect, though.

```python
text = get_body_text(page)
```

## Get the raw text of the body

Get the raw text of the body. This will include all the tags and divs and things.

```python
text = get_body_text_raw(page)
```

# Advanced Usage

## Get browser

This will give you a reference to the browser object, which you can use for advanced stuff. The browser object comes from Pyppeteer, so anything you can do with Pyppeteer, you can do with this.

```python
browser = get_browser()
```

## Evaluate Javascript

Call some Javascript on the page. Equivalent of opening the console and typing in some Javascript.

```python
result = evaluate_javascript(page, "document.title")
```

## Initialize browser

This will initialize the browser object. You can pass `headless` and `executable_path`. Headless will control whether the actual window appears on screen. Executable path will control which browser is used. By default, it will try to find Chrome first, then fall back to Chromium if it can't find Chrome.

The browser will be auto-initialized by default so you don't need to call this. The only reason you would is because you want to use headful or swap the browser.

```python
init_browser(headless=True, executable_path="/path/to/chrome")
```

```bash
bash publish.sh --version=<version> --username=<pypi_username> --password=<pypi_password>
```

# Contributions Welcome

If you like this library and want to contribute in any way, please feel free to submit a PR and I will review it. Please note that the goal here is simplicity and accesibility, using common language and few dependencies.

# Questions, Comments, Concerns

If you have any questions, please feel free to reach out to me on [Twitter](https://twitter.com/spatialweeb) or [Discord](@new.moon).
