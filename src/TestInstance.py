import pytest
from playwright.sync_api import sync_playwright

from src.enums.BrowserTypes import BrowserTypes


@pytest.fixture(scope="module")
def playwright_context(request):
    with sync_playwright() as p:
        if request.param == BrowserTypes.CHROMIUM.value:
            browser = p.chromium.launch(headless=False)
        elif request.param == BrowserTypes.FIREFOX.value:
            browser = p.firefox.launch(headless=False)
        elif request.param == BrowserTypes.WEBKIT.value:
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {request.param}")

        context = browser.new_context()
        context.set_default_timeout(10000)  # Set a global timeout of 10 seconds for all actions
        yield context
        browser.close()
