"""Obtain information about device."""
from scrapli.driver.core import IOSXEDriver
import re

interfaces = dict()  # Enabled interfaces
ssh_sessions = dict()  # Active SSH sessions

device = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": "developer",
        "auth_password": "C1sco12345",
        "auth_strict_key": False
}

connection = IOSXEDriver(**device)
connection.open()

# Get hostname, uptime & interfaces count
version = connection.send_command("show version").genie_parse_output()
hostname = version["version"]["hostname"]
uptime = version["version"]["uptime"]
interfaces_count = version["version"]["number_of_intfs"]["Gigabit Ethernet"]

# Get domain name & who made the last configuration changes and when
domain = re.findall(r"(?<=domain is ).*", connection.send_command("show hosts").result)[0]
last_conf_change = re.findall(r"(?<=Last configuration change at ).*", connection.send_command("show running-config").result)[0]

# Get all enabled interfaces, their IPs and MAC addresses
brief = connection.send_command("show ip interface brief").genie_parse_output()
for interface, params in brief["interface"].items():
    if params["status"] != "up":
        continue

    info = connection.send_command(f"show interfaces {interface}").genie_parse_output()

    if "mac_address" in info[interface]:
        interfaces[interface] = {"ip": params["ip_address"], "mac": info[interface]["mac_address"]}

# Check if SSH access is enabled
ssh_status = "Enabled" if "SSH Enabled" in connection.send_command("show ip ssh").result else "Disabled"

# Get all active SSH sessions and their IPs
users = connection.send_command("show users").genie_parse_output()
for params in users["line"].values():
    ssh_sessions[params["user"]] = params["location"]

# Get total IP packets sent & received
traffic = connection.send_command("show ip traffic").genie_parse_output()
sent = traffic["ip_statistics"]["ip_sent_generated"]
received = traffic["ip_statistics"]["ip_rcvd_total"]

# Export the extracted data to a CSV file
with open("device_data.csv", "w") as file:
    file.write(f"Hostname,{hostname}\n")
    file.write(f"Domain,{domain}\n")
    file.write(f"Last configuration changes,{last_conf_change}\n")
    file.write(f"Uptime,{uptime}\n")
    file.write(f"Interfaces,{interfaces_count}\n")
    file.write(f"Enabled interfaces,{len(interfaces)}\n")
    file.write(f"interface,IP,MAC\n")
    for interface, values in interfaces.items():
        file.write(f"{interface},{values['ip']},{values['mac']}\n")
    file.write(f"SSH access,{ssh_status}\n")
    file.write(f"SSH sessions,{len(ssh_sessions)}\n")
    file.write(f"Client,IP\n")
    for client, ip in ssh_sessions.items():
        file.write(f"{client},{ip}\n")
    file.write(f"Sent packets,{sent}\n")
    file.write(f"Received packets,{received}")

# Print the extracted data to console
print("Hostname:", hostname)
print("Domain:", domain)
print("Last configuration changes:", last_conf_change)
print("Uptime:", uptime)
print("Interfaces:", interfaces_count)
print("Enabled interfaces:", len(interfaces))
for interface, values in interfaces.items():
    print(f"\t- {interface} [IP: {values['ip']}] [MAC: {values['mac']}]")
print("SSH access:", ssh_status)
print("SSH sessions:", len(ssh_sessions))
for client, ip in ssh_sessions.items():
    print(f"\t- {client} [IP: {ip}]")
print("IP packets sent:", sent)
print("IP packets received:", received)

connection.close()
