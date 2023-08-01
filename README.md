# agentbrowser <a href="https://discord.gg/qetWd7J9De"><img style="float: right" src="https://dcbadge.vercel.app/api/server/qetWd7J9De" alt=""></a>

A browser for your agent, built on Playwright.

<img src="resources/image.jpg">

[![Lint and Test](https://github.com/AutonomousResearchGroup/agentbrowser/actions/workflows/test.yml/badge.svg)](https://github.com/AutonomousResearchGroup/agentbrowser/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/agentbrowser.svg)](https://badge.fury.io/py/agentbrowser)

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
    get_document_html,
    create_page,
    close_page,
    evaluate_javascript,
)
```

## Quickstart

```python
from agentbrowser import (
    navigate_to,
    get_body_text,
)

# Navigate to a URL
page = navigate_to("https://google.com")

# Get the text from the page
text = get_body_text(page)

print(text)
```

## API Documentation

### `ensure_event_loop()`

Ensure that there is an event loop in the current thread. If no event loop exists, a new one is created and set for the current thread. This function returns the current event loop.

Example usage:

```python
loop = ensure_event_loop()
```

### `get_browser()`

Get a Playwright browser. If the browser doesn't exist, initializes a new one.

Example usage:

```python
browser = get_browser()
```

### `init_browser(headless=True, executable_path=None)`

Initialize a new Playwright browser.

Parameters:

- `headless`: Whether the browser should be run in headless mode, defaults to True.
- `executable_path`: Path to a Chromium or Chrome executable to run instead of the bundled Chromium.

Example usage:

```python
init_browser(headless=False, executable_path="/usr/bin/google-chrome")
```

### `create_page(site=None)`

Create a new page in the browser. If a site is provided, navigate to that site.

Parameters:

- `site`: URL to navigate to, defaults to None.

Example usage:

```python
page = create_page("https://www.example.com")
```

### `close_page(page)`

Close a page.

Parameters:

- `page`: The page to close.

Example usage:

```python
page = create_page("https://www.example.com")
close_page(page)
```

### `navigate_to(url, page, wait_until="domcontentloaded")`

Navigate to a URL in a page.

Parameters:

- `url`: The URL to navigate to.
- `page`: The page to navigate in.

Example usage:

```python
page = create_page()
navigate_to("https://www.example.com", page)
```

### `get_document_html(page)`

Get the HTML content of a page.

Parameters:

- `page`: The page to get the HTML from.

Example usage:

```python
page = create_page("https://www.example.com")
html = get_document_html(page)
print(html)
```

### `get_page_title(page)`

Get the title of a page.

Parameters:

- `page`: The page to get the title from.

Example usage:

```python
page = create_page("https://www.example.com")
title = get_page_title(page)
print(title)
```

### `get_body_text(page)`

Get the text content of a page's body.

Parameters:

- `page`: The page to get the text from.

Example usage:

```python
page = create_page("https://www.example.com")
text = get_body_text(page)
print(text)
```

### `get_body_html(page)`

Get the HTML content of a page's body.

Parameters:

- `page`: The page to get the HTML from.

Example usage:

```python
page = create_page("https://www.example.com")
body_html = get_body_html(page)
print(body_html)
```

### `screenshot_page(page)`

Get a screenshot of a page.

Parameters:

- `page`: The page to screenshot.

Example usage:

```python
page = create_page("https://www.example.com")
screenshot = screenshot_page(page)
with open("screenshot.png", "wb") as f:
    f.write(screenshot)
```

### `evaluate_javascript(code, page)`

Evaluate JavaScript code in a page.

Parameters:

- `code`: The JavaScript code to evaluate.
- `page`: The page to evaluate the code in.

Example usage:

```python
page = create_page("https://www.example.com")
result = evaluate_javascript("document.title", page)
print(result)
```

### `find_chrome()`

Find the Chrome executable. Returns the path to the Chrome executable, or None if it could not be found.

Example usage:

```python
chrome_path = find_chrome()
print(chrome_path)
```

# Contributions Welcome

If you like this library and want to contribute in any way, please feel free to submit a PR and I will review it. Please note that the goal here is simplicity and accesibility, using common language and few dependencies.
