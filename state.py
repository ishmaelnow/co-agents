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