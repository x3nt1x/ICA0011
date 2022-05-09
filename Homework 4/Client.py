"""SOAP client."""
from suds.client import Client

client = Client("http://localhost:8000/?wsdl", cache=None)

print("Task 1:")
print(client.service.get_os())
print(client.service.get_ip())
print(client.service.check_host("www.google.com"), "\n")

print("Task 2:")
print(client.service.get_domain_name_servers("google.com"), "\n")
print(client.service.get_domain_dns_a_record("google.com"), "\n")
print(client.service.get_domain_mx_records("google.com"), "\n")

print("Task 3:")
print(client.service.get_disk_usage("/home"))
