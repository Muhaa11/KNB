import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC91b68fc9c952c1c4c2b5bfccca3d6a31'
auth_token = '94aa4099f15c45b279870ef37f4135e5'
client = Client(account_sid, auth_token)
def send_sms(code, phone_number, username):
    message = client.messages.create(
                              body=f'Hi there {username}! Your verification code is {code}',
                              from_='+14695356876',
                              to=f'{phone_number}'
                          )

    print(message.sid)