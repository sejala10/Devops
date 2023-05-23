import smtplib
from email.message import EmailMessage
from configparser import ConfigParser
def read_config():
    config = ConfigParser()
    config.read("C:\\Users\\ThinkPad\\OneDrive - kasmo.co\\Desktop\\migration1.config")
    sender = config.get('EMAIL','sender')
    password = config.get ('EMAIL', 'password')
    subject = config.get('EMAIL','subject')
    receiver = config.get('EMAIL','receiver')
    print(sender, password, subject, receiver)
    return sender, password, subject, receiver

def email_alert(subject, body, to, sender, password):
    print(sender)
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = sender
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    sender, password, subject, receiver = read_config()
    email_alert(subject, "hello,  have a teriffic tuesday!-", receiver, sender, password)
#print(config.sections())
#print(list(migraton.config['EMAIL']))