import fbchat
from fbchat import Client
from fbchat.models import *
client = Client('<email address> ', '<password>')

users = client.searchForUsers('<user name of your friend>')
user = users[0]

msg = "put the message here"
i = 1
while i<=100:
    sent = client.send(fbchat.models.Message(msg),user.uid)
    i+=1
###################### ☠ Try this at your own risk ☠ ###########
# while True:
#     sent = client.send(fbchat.models.Message(msg),user.uid)
    
client.logout()