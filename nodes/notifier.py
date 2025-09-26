import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from state import SecretaryState

load_dotenv()

def notify(state: SecretaryState) -> SecretaryState:
    # Load credentials from .env
    host = os.getenv("EMAIL_HOST")
    port = int(os.getenv("EMAIL_PORT"))
    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    # Compose the email
    msg = EmailMessage()
    msg["Subject"] = "Generated Letter from Secretary Agent"
    msg["From"] = sender
    msg["To"] = state.email or sender  # fallback to self if no recipient
    msg.set_content(state.formatted_letter or state.letter or "No content available.")

    # Send the email
    try:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        notification = f"📧 Email successfully sent to {msg['To']} at {state.timestamp or 'unspecified time'}."
    except Exception as e:
        notification = f"❌ Email failed: {str(e)}"

    return state.copy(update={"notification": notification})