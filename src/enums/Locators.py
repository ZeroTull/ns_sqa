from enum import Enum


class GoogleLocators(Enum):
    GOOGLE_URL = "https://www.google.com"
    GOOGLE_INPUT_FIELD_LOCATOR = "//*[@name='q']"
    ACCEPT_ALL = "//div[text()='Accept all']"
    NAME_RESULT_LOCATOR = "//h3[text()='Name']"
    CHOOSE_LANGUAGE_BUTTON = "//*[@id='vc3jof']"
    LANGUAGE_OPTION = "//*[contains(@data-hl, '{language_code}')]"
