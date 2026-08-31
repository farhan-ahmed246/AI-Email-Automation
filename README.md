# AI Email Automation

An AI-powered email automation API that generates professional replies from incoming emails and can send those replies through SMTP.

## Features

- Generate AI email replies with a simple API endpoint
- Adjustable reply tone and optional business context
- Send generated replies through SMTP
- Environment-variable based secrets (no API keys in source code)
- FastAPI + OpenAI integration

## Project structure

```text
.
├── app.py
├── ai_service.py
├── email_service.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your OpenAI and SMTP credentials.

3. Start the API:

```bash
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## API

### Generate a reply

`POST /generate-reply`

```json
{
  "sender_name": "John",
  "original_email": "Hi, I would like to know more about your service.",
  "tone": "professional",
  "context": "We offer a free discovery call."
}
```

### Generate and send a reply

`POST /send-reply`

Uses the same fields plus `recipient` and `subject`. SMTP credentials must be configured in the environment.

## Security

Never commit `.env` or real API keys/passwords. Use `.env.example` only as a template and configure secrets through your local environment or deployment platform.
