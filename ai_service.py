"""LLM integration for generating email replies."""

import os


def generate_reply(sender_name: str, original_email: str, tone: str, context: str | None = None) -> str:
    """Generate a reply using OpenAI when configured, otherwise fail clearly."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    extra_context = f"\nAdditional context: {context}" if context else ""
    prompt = (
        f"Write a concise {tone} business email reply to {sender_name}.\n"
        f"Original email:\n{original_email}{extra_context}\n"
        "Return only the email body. Do not invent facts, promises, prices, or dates."
    )
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
        input=prompt,
    )
    return response.output_text.strip()
