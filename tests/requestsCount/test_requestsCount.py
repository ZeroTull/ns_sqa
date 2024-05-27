import allure
import pytest

from src.TestInstance import playwright_context
from src.enums.BrowserTypes import BrowserTypes
from src.enums.Locators import GoogleLocators
from src.pages.GoogleSearchPage import GoogleSearchPage

# Dictionaries to store requests counts by type
google_request_counter = {}
first_result_request_counter = {}
target_page_request_counter = {}
SEARCH_VALUE = "name"
English = "en-US"


@allure.feature('Google Search')
@allure.story('Count requests per page')
@pytest.mark.parametrize("playwright_context", BrowserTypes.BROWSER_TYPES, indirect=True)
def test_requests_count(playwright_context):
    (GoogleSearchPage.go_to_google_search_page(playwright_context.new_page())
     .select_language_and_accept_cookies(English)
     .count_requests(google_request_counter)
     .search(SEARCH_VALUE)
     .count_requests(first_result_request_counter)
     .navigate_to(GoogleLocators.NAME_RESULT_LOCATOR)
     .count_requests(target_page_request_counter))

    print_results_by_type(google_request_counter, "request counts by type for Google search page:")
    print_results_by_type(first_result_request_counter, "request counts by type for the search results page:")
    print_results_by_type(target_page_request_counter, "request counts by type for the Wiki page:")

    # Print the number of requests
    print(f"\nTotal number of requests: {sum(first_result_request_counter.values()) + sum(google_request_counter.values()) + sum(target_page_request_counter.values())}")

    # Return the counts for further assertions or use
    return google_request_counter, first_result_request_counter, target_page_request_counter


def print_results_by_type(counter={}, message=""):
    with allure.step(f'\nPrint {message}'):
        print(f"\n{message}")
    for resource_type, count in counter.items():
        print(f"{resource_type}: {count}")
