import requests
from twilio.rest import Client
import time

def sms(message):
    account_sid = '<YOUR_TWILIO_ACCOUNT_SID>'
    auth_token = '<YOUR_TWILIO_ACCOUNT_AUTH_TOKEN>'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_='<YOUR TWILIO NUMBER>',
            to='<YOUR PERSONAL VERIFIED NUMBER WITH TWILIO>'
        )
    print(message.sid)

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=455118&date=16-06-2021'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
print("BOT Running......")
while True:
    result = requests.get(url, headers=headers).json()
    try:
        l1 = result["sessions"]
        print(l1)
        l2 = l1[2]
        slot1 = l2['available_capacity_dose1']
        slot2 = l2['available_capacity']
        if slot1 > 0 or slot2 > 0:
            message = "From local : Slot available " + str(slot1) +" "+ str(slot2)
            sms(message)
    except:
        print("fails")
    time.sleep(30)