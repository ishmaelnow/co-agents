from state import SecretaryState

def route_task(state: SecretaryState) -> SecretaryState:
    task = state.task.lower()

    # Basic keyword-based routing
    if any(keyword in task for keyword in ["weather", "forecast", "temperature"]):
        route = "weather_only"
    elif any(keyword in task for keyword in ["define", "explain", "summarize", "describe"]):
        route = "minimal"
    else:
        route = "full"

    return state.copy(update={"route": route})