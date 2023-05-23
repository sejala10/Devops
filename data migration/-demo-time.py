import pywhatkit
from datetime import datetime
from configparser import ConfigParser
def read_config():
    config = ConfigParser()
    config.read("C:\\Users\\ThinkPad\\OneDrive - kasmo.co\\Desktop\\migration1.config")
    recipient_nos = config.get('WHATSAPP','recipient_nos')
    #read_config() == recipient_nos
    print(recipient_nos)
    return recipient_nos
    
'''
# datetime object containing current date and time
now = datetime.now()lets being the week marvelously 
lets being the week marvelously 

 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
'''
recipient_nos = read_config()
pywhatkit.sendwhatmsg_to_group_instantly(recipient_nos ,'hii')

