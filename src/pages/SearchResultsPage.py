import allure
from playwright.sync_api import Page
from src.enums.Locators import GoogleLocators
from src.helpers.Counter import Counter
from src.pages.GoogleSearchPage import GoogleSearchPage


class SearchResultsPage:

    def __init__(self, page: Page):
        self.page = page

    def count_requests(self, request_counter: dict):
        # Count requests for the current page
        Counter.count_requests_for_page(self.page, request_counter)
        return self

    def navigate_to_first_result(self, locator):
        with allure.step(f'Navigate to {locator.name}'):
            # Click on the first result found by the locator
            first_result = self.page.locator(locator.value).first
            first_result.click()
        return GoogleSearchPage(self.page)
