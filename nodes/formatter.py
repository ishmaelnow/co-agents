from state import SecretaryState

def format_letter(state: SecretaryState) -> SecretaryState:
    letter = state.letter or ""

    # Use values from state or fallback defaults
    replacements = {
        "[Your Name]": state.sender_name or "Ali Smith",
        "[Your Position]": state.sender_position or "Company Secretary",
        "[Company Name]": state.company_name or "NeuroEdge Inc.",
        "[Company Address]": state.company_address or "123 Innovation Blvd",
        "[City, State, ZIP]": state.city_state_zip or "Lewisville, TX 75057",
        "[Email Address]": state.email or "ali.smith@neuroedge.com",
        "[Phone Number]": state.phone or "(555) 123-4567",
        "[Date]": state.timestamp or "September 26, 2025",
        "[Recipient's Name]": state.recipient_name or "Dr. Jordan"
    }

    for placeholder, value in replacements.items():
        letter = letter.replace(placeholder, value)

    return state.copy(update={"formatted_letter": letter})