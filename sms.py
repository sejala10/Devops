import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
phone_number = os.getenv("PHONE_NUMBER")
TWILIO_ACCOUNT_SID = 'ACc730882d0884be635be6e28e5e8908e7'
TWILIO_AUTH_TOKEN = '8bef01a8afa29451401f77f84f792b31'

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+917277745999',
                     to='+916303595458'
                 )
print("SMS has been sent")
print(message.sid)