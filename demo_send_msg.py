import requests

def send_message(api_key, phone_number, message):
    url = "https://app.instasent.com/user/token/"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": phone_number,
        "text": message
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send the message.")
        print("Response:", response.text)

# Set your Instasent API key, phone number, and message content
api_key = "d353b54b2d8f8ad4723a2d30ba51206745db646d"
phone_number = 6303595458
message = "Hello, World!"

# Call the function to send the message
send_message(api_key, phone_number, message)
