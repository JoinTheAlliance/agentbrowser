"""
agentbrowser

Simple agent memory, powered by chromadb
"""

__version__ = "0.1.0"
__author__ = "Moon (https://github.com/lalalune)"
__credits__ = "https://github.com/lalalune/agentbrowser"

from .browser import (
    get_browser,
    init_browser,
    create_page,
    close_page,
    navigate_to,
    get_body_text,
    get_document_html,
    get_body_html,
    evaluate_javascript
)

__all__ = [
    "get_browser",
    "init_browser",
    "create_page",
    "navigate_to",
    "close_page",
    "get_document_html",
    "get_body_text",
    "get_body_html",
    "evaluate_javascript",
]
