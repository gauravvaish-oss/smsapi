from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, WHATSAPP_FROM

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp(to: str, message: str):
    wa = client.messages.create(
        body=message,
        from_=WHATSAPP_FROM,
        to=f"whatsapp:{to}"
    )
    return wa.sid
