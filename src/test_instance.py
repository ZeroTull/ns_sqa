# test_instance.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def playwright_context(request):
    with sync_playwright() as p:
        if request.param == 'chromium':
            browser = p.chromium.launch(headless=False)
        elif request.param == 'firefox':
            browser = p.firefox.launch(headless=False)
        elif request.param == 'webkit':
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {request.param}")

        context = browser.new_context()
        context.set_default_timeout(10000)  # Set a global timeout of 10 seconds for all actions
        yield context
        browser.close()
