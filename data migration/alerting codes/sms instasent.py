"""import instasent
import response
client = instasent.Client('8445b2c78605753c546d6922e6273514349fceb7')
#client = instasent.Client("+917277745999")
response = client.send_sms('Mi company', '+916303595458', 'good morning')

print (response["response_code"])
print (response["response_body"])

instasent.send_sms(+917277745999, +916303595458,'Good morning')
instasent.get_sms(1, 5)
instasent.get_sms_by_id(5146712)"""
import requests
import instasent
response = instasent.(+916303595458,+919145494994,'Swaraj is cute')
message_id = response['message_id']
print(message_id)
'''
# Replace YOUR_API_KEY with your actual API key from Instasent
API_KEY = '8445b2c78605753c546d6922e6273514349fceb7'

# Replace these values with your desired recipient and message text
recipient = '+916303595458'
message = 'Hello, this is a test message sent via Instasent!'

# Build the request URL and payload
url = 'https://api.instasent.com/sms'
payload = {
    'to': recipient,
    'text': message,
    'from': '', # replace this with your own Sender ID
}

# Add the API key to the headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

# Send the request and print the response
response = requests.post(url, headers=headers, json=payload)
print(response.json())


'''