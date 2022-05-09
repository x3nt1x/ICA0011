"""SOAP server."""
import shutil
import platform
import netifaces
import subprocess
import dns.resolver
from spyne import Application, ServiceBase, String, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class SOAPService(ServiceBase):
    """SOAP service."""

    @rpc(_returns=String)
    def get_os(self) -> str:
        """Get operating system's name."""
        return f"I am using {platform.system()} Platform"

    @rpc(_returns=String)
    def get_ip(self) -> str:
        """Get user’s machine IP address."""
        return f"My IP address is {netifaces.ifaddresses('enp0s3')[netifaces.AF_INET][0]['addr']}"

    @rpc(String, _returns=String)
    def check_host(self, host: str) -> str:
        """Test host reachability."""
        ping_char = "-n" if platform.system() == "Windows" else "-c"
        response = subprocess.call(["ping", ping_char, "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return f"and {host} is {'reachable' if response == 0 else 'unreachable'}"

    @rpc(String, _returns=String)
    def get_domain_name_servers(self, domain: str) -> str:
        """Get domain's name servers."""
        name_servers = dns.resolver.resolve(domain, 'NS')
        output = '\n'.join(map(str, name_servers))
        return f"The Name Servers (NS) of {domain}:\n{output}"

    @rpc(String, _returns=String)
    def get_domain_dns_a_record(self, domain: str) -> str:
        """Get domain's DNS A record."""
        a_record = dns.resolver.resolve(domain, 'A')
        output = '\n'.join(map(str, a_record))
        return f"The DNS A Record of {domain}:\n{output}"

    @rpc(String, _returns=String)
    def get_domain_mx_records(self, domain: str) -> str:
        """Get domain's MX records."""
        mx_records = dns.resolver.resolve(domain, 'MX')
        output = '\n'.join(map(str, mx_records))
        return f"The MX Records of {domain}:\n{output}"

    @rpc(String, _returns=String)
    def get_disk_usage(self, path: str) -> str:
        """Get path's disk usage."""
        disk_usage = shutil.disk_usage(path)
        total = f"Total: {disk_usage.total // (2 ** 30)}GB"
        used = f"Used: {disk_usage.used // (2 ** 30)}GB"
        free = f"Free: {disk_usage.free // (2 ** 30)}GB"

        return f"{total}\n{used}\n{free}"


app = WsgiApplication(Application([SOAPService], "tns", in_protocol=Soap11(), out_protocol=Soap11()))

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()
