from twilio.rest import Client

# Twilio account SID and auth token
account_sid = "ACc730882d0884be635be6e28e5e8908e7"
auth_token = "8bef01a8afa29451401f77f84f792b31"

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS
def send_sms(from_number, to_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print("SMS sent successfully!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("Failed to send SMS:", str(e))

# Provide the necessary information
from_number = "+12706123698"  # Should be in E.164 format, e.g., +1234567890
to_number = "+916303595458"  # Should be in E.164 format, e.g., +9876543210
message = "Hello, this is a test SMS from Python!"

# Send the SMS
send_sms(from_number, to_number, message)
