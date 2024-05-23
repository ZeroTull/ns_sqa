import pytest
import allure
from time import time
from playwright.sync_api import Page
from src.enums.dnsservers import DnsServers


@allure.feature("Web Performance")
@allure.story("Page Load Time Test")
@pytest.mark.parametrize("dns_server", DnsServers.DNS_SERVERS)
def test_page_load_time(dns_server, page: Page):
    with allure.step(f"Go to Google homepage using DNS server {dns_server}"):
        page.goto("https://www.google.com")

    with allure.step("Measure page load time"):
        start_time = time()
        page.wait_for_selector("//*[@alt='Google']")
        end_time = time()

    page_title = page.title()
    load_time = (end_time - start_time) * 1000  # Convert to milliseconds

    with allure.step("Log and attach page load time"):
        allure.attach(f"DNS Server: {dns_server}", name="DNS Server", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Page Load Time: {load_time:.2f} ms", name="Page Load Time",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Page Title: {page_title}", name="Page Title", attachment_type=allure.attachment_type.TEXT)

        print(f"\nDNS Server: {dns_server}")
        print("Page load time: {:.2f} ms".format(load_time))
