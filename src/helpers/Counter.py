import time

import allure
from playwright.async_api import Page


def count_requests_by_type(request, request_counter: {}):
    resource_type = request.resource_type
    if resource_type in request_counter:
        request_counter[resource_type] += 1
    else:
        request_counter[resource_type] = 1


class Counter:
    @staticmethod
    def count_requests_for_page(page: Page, request_counter: {}):
        time.sleep(0.5)
        with allure.step(f'Count requests for {page.title()} page'):
            page.on("request", lambda request: count_requests_by_type(request, request_counter))
