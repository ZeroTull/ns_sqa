import pytest
import allure
import speedtest

from src.enums.DnsServers import DnsServers


@allure.feature("Network Performance")
@allure.story("Speed and Latency Test")
@pytest.mark.parametrize("dns_server", DnsServers.DNS_SERVERS)
def test_perform_speed_latency(dns_server):
    with allure.step(f"Initialize Speedtest with DNS server {dns_server}"):
        st = speedtest.Speedtest()

    with allure.step("Perform download and upload test"):
        st.download()
        st.upload()

    res = st.results.dict()

    download_speed = res["download"] / 1000000  # Convert to Mbps
    upload_speed = res["upload"] / 1000000  # Convert to Mbps
    latency = res["ping"]

    with allure.step("Log and attach speed test results"):
        allure.attach(f"DNS Server: {dns_server}", name="DNS Server", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Download Speed: {download_speed:.2f} Mbps", name="Download Speed",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Upload Speed: {upload_speed:.2f} Mbps", name="Upload Speed",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Latency: {latency:.2f} ms", name="Latency", attachment_type=allure.attachment_type.TEXT)

        print(f"\nDNS Server: {dns_server}")
        print("Download Speed: {:.2f} Mbps".format(download_speed))
        print("Upload Speed: {:.2f} Mbps".format(upload_speed))
        print("Latency: {:.2f} ms".format(latency))
