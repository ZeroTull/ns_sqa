import http.client as httplib
import pytest

from src.enums.DnsServers import DnsServers


@pytest.mark.parametrize("dns_server", DnsServers.DNS_SERVERS)
def test_have_internet(dns_server) -> bool:
    conn = httplib.HTTPSConnection(dns_server)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()
