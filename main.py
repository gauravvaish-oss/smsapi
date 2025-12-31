from fastapi import FastAPI
from pydantic import BaseModel

from services.sms_service import send_sms
from services.whatsapp_service import send_whatsapp

app = FastAPI()

class MessageRequest(BaseModel):
    to: str
    message: str


@app.post("/send-sms")
def sms_api(data: MessageRequest):
    sid = send_sms(data.to, data.message)
    return {"status": "sent", "type": "sms", "sid": sid}


@app.post("/send-whatsapp")
def whatsapp_api(data: MessageRequest):
    sid = send_whatsapp(data.to, data.message)
    return {"status": "sent", "type": "whatsapp", "sid": sid}
