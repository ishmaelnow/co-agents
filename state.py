from typing import Optional
from pydantic import BaseModel

class SecretaryState(BaseModel):
    task: str  # ✅ Plain string again
    letter: Optional[str] = None
    reflection: Optional[str] = None
    evaluation: Optional[str] = None
    weather: Optional[str] = None
    search_result: Optional[str] = None
    api_result: Optional[str] = None
    search_reflection: Optional[str] = None
    timestamp: Optional[str] = None  # ✅ New field
    formatted_letter: Optional[str] = None  # ✅ New field

    sender_name: Optional[str] = None
    sender_position: Optional[str] = None
    company_name: Optional[str] = None
    company_address: Optional[str] = None
    city_state_zip: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    recipient_name: Optional[str] = None
    formatted_letter: Optional[str] = None
    route: Optional[str] = None  # e.g. "full" or "minimal"
    notification: Optional[str] = None  # e.g. "Letter sent to Slack", "Logged to file"
