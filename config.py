import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

SMS_FROM = os.getenv("TWILIO_SMS_FROM")
WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
