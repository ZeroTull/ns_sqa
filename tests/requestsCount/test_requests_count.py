import allure
import pytest
from playwright.sync_api import sync_playwright

from src.pages.google_search_page import GoogleSearchPage
from src.enums.locators import GoogleLocators
from src.enums.browsers import Browser_Types
from src.helpers.counter import Counter

# Dictionaries to store requests counts by type
google_request_counter = {}
first_result_request_counter = {}
target_page_request_counter = {}
SEARCH_VALUE = "name"
English = "en-US"


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
        # Set a global timeout of 10 seconds for all actions
        context.set_default_timeout(10000)
        yield context


@allure.feature('Google Search')
@allure.story('Count requests per page')
@pytest.mark.parametrize("playwright_context", Browser_Types.BROWSER_TYPES, indirect=True)
def test_requests_count(playwright_context):
    page = playwright_context.new_page()

    # Go to address and accept cookies
    GoogleSearchPage.go_to_google_search_page(page) \
        .select_language_and_accept_cookies(page, English)

    # Count requests count for the first page
    Counter.count_requests_for_page(page, google_request_counter)
    # Search for data
    GoogleSearchPage.search(page, SEARCH_VALUE)

    # Count requests for search result page
    Counter.count_requests_for_page(page, first_result_request_counter)

    # Go to Wiki Name page
    GoogleSearchPage.navigate_to(page, GoogleLocators.NAME_RESULT_LOCATOR)

    # Get request count for the target page
    Counter.count_requests_for_page(page, target_page_request_counter)

    print_results_by_type(google_request_counter, "request counts by type for Google search page:")
    print_results_by_type(first_result_request_counter, "request counts by type for the search results page:")
    print_results_by_type(target_page_request_counter, "request counts by type for the Wiki page:")

    # Print the number of requests
    print(
        f"\nTotal number of requests: {sum(first_result_request_counter.values()) + sum(google_request_counter.values()) + sum(target_page_request_counter.values())}")

    # Return the counts for further assertions or use
    return google_request_counter, first_result_request_counter, target_page_request_counter


def print_results_by_type(counter={}, message=""):
    with allure.step(f'\nPrint {message}'):
        print(f"\n{message}")
    for resource_type, count in counter.items():
        print(f"{resource_type}: {count}")
