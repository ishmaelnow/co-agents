from datetime import datetime
from state import SecretaryState

def inject_timestamp(state: SecretaryState) -> SecretaryState:
    now = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    return state.copy(update={"timestamp": now})