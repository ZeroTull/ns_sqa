from enum import Enum

import allure
from playwright.async_api import Page

from src.enums.Locators import GoogleLocators
from src.helpers.Counter import Counter


class GoogleSearchPage:

    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def go_to_google_search_page(page: Page):
        with (allure.step('Navigate to Google')):
            page.goto(GoogleLocators.GOOGLE_URL.value)
            return GoogleSearchPage(page)

    def select_language_and_accept_cookies(self, code: str):
        with (allure.step('Accept cookies')):
            self.page.goto(GoogleLocators.GOOGLE_URL.value)
            self.page.locator(GoogleLocators.CHOOSE_LANGUAGE_BUTTON.value).click()
            self.page.locator(GoogleLocators.LANGUAGE_OPTION.value.format(language_code=code)).click()
            self.page.locator(GoogleLocators.ACCEPT_ALL.value).click()
        return self

    def search(self, data_to_search: str):
        with allure.step(f'Search for data: {str}'):
            search_input = self.page.locator(GoogleLocators.GOOGLE_INPUT_FIELD_LOCATOR.value)
            search_input.fill(data_to_search)
            self.page.keyboard.press('Enter')
        return self

    def navigate_to(self, locator: Enum):
        with allure.step(f'Navigate to {locator.name}'):
            name_result = self.page.locator(locator.value).first
            name_result.click()
        return self

    def count_requests(self, request_counter: {}):
        Counter.count_requests_for_page(self.page, request_counter)
        return self
