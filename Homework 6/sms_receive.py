"""Handle received SMS messages."""
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_receive():
    """Listen for SMS replies."""

    # Run received command
    message = request.values.get('Body', None)
    os.system(message)

    # Send SMS reply
    response = MessagingResponse()
    response.message(f"Running command: {message}")

    return str(response)


if __name__ == "__main__":
    app.run()
