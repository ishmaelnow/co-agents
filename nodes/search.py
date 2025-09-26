from state import SecretaryState
from langchain_community.tools import DuckDuckGoSearchResults  # ✅ Updated import

search_tool = DuckDuckGoSearchResults()

def search_web(state: SecretaryState) -> SecretaryState:
    query = state.task
    result = search_tool.run(query)
    return state.copy(update={"search_result": result})