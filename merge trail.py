import smtplib
import pywhatkit
from email.message import EmailMessage
from datetime import datetime

def whatsap():
# Send WhatsApp message
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and time =", dt_string)
    pywhatkit.sendwhatmsg_to_group_instantly("+917277745999", "Let's begin the week marvelously")

# Send Email
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "sejuambati@gmail.com"
    msg['from'] = user
    password = "fdglpnshncmnqntv"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    
    if __name__ == '__main__':
        email_alert("Hey - Subject", "Hello, have a marvolus monday!", "Ppatukurianjali@gmail.com")