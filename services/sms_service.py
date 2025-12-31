from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, SMS_FROM

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(to: str, message: str):
    sms = client.messages.create(
        body=message,
        from_=SMS_FROM,
        to=to
    )
    return sms.sid
