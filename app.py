"""AI Email Automation API.

Generates professional email replies with an LLM and optionally sends them
through SMTP. Secrets are read from environment variables only.
"""

import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

from ai_service import generate_reply
from email_service import send_email

app = FastAPI(title="AI Email Automation", version="1.0.0")


class ReplyRequest(BaseModel):
    sender_name: str = "Customer"
    original_email: str
    tone: str = "professional"
    context: Optional[str] = None


class SendRequest(ReplyRequest):
    recipient: EmailStr
    subject: str


@app.get("/")
def root():
    return {"name": "AI Email Automation", "status": "running"}


@app.post("/generate-reply")
def create_reply(request: ReplyRequest):
    try:
        reply = generate_reply(
            sender_name=request.sender_name,
            original_email=request.original_email,
            tone=request.tone,
            context=request.context,
        )
        return {"reply": reply}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/send-reply")
def send_reply(request: SendRequest):
    try:
        reply = generate_reply(
            sender_name=request.sender_name,
            original_email=request.original_email,
            tone=request.tone,
            context=request.context,
        )
        send_email(str(request.recipient), request.subject, reply)
        return {"message": "Email sent successfully", "reply": reply}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
