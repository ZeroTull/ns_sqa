from enum import Enum

import allure
from playwright.async_api import Page

from src.enums.locators import GoogleLocators


class GoogleSearchPage:

    @staticmethod
    def go_to_google_search_page(page: Page):
        with (allure.step('Navigate to Google')):
            page.goto(GoogleLocators.GOOGLE_URL.value)
            return GoogleSearchPage

    @staticmethod
    def select_language_and_accept_cookies(page: Page, code: str):
        with (allure.step('Accept cookies')):
            page.goto(GoogleLocators.GOOGLE_URL.value)
            page.locator(GoogleLocators.CHOOSE_LANGUAGE_BUTTON.value).click()
            page.locator(GoogleLocators.LANGUAGE_OPTION.value.format(language_code=code)).click()
            page.locator(GoogleLocators.ACCEPT_ALL.value).click()
            return GoogleSearchPage

    @staticmethod
    def search(page: Page, data_to_search: str):
        with allure.step('Search for data'):
            search_input = page.locator(GoogleLocators.GOOGLE_INPUT_FIELD_LOCATOR.value)
            search_input.fill(data_to_search)
            page.keyboard.press('Enter')

    @staticmethod
    def navigate_to(page: Page, locator: Enum):
        with allure.step(f'Navigate to {locator.name}'):
            name_result = page.locator(locator.value).first
            name_result.click()
