import smtplib
from email.message import EmailMessage

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
     email_alert("hey-subject", "hello," "have a marvalous monday!-", "Ppatukurianjali@gmail.com")