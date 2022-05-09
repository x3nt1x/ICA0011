"""Check server status and notify via SMS."""
import time
import requests
from twilio.rest import Client


def is_server_running(ip: str) -> bool:
    """Check if server is up and running."""
    try:
        if requests.get(ip).status_code == 200:
            return True
    except Exception:
        return False


def send_sms():
    """Send SMS notification."""
    client = Client("account_sid", "auth_token")

    client.messages.create(
        messaging_service_sid='service_sid',
        body='The Web Server is Down!',
        to='phone_number'
    )


if __name__ == "__main__":
    while True:
        if not is_server_running("http://127.0.0.1"):
            send_sms()

        # Check server status every 30 minutes
        time.sleep(1800)
