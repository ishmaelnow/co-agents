from langgraph.graph import StateGraph
from state import SecretaryState

# Import all agent nodes
from nodes.search import search_web
from nodes.weather import check_weather
from nodes.search_reflector import reflect_search
from nodes.timestamp import inject_timestamp
from nodes.generator import generate
from nodes.reflector import reflect
from nodes.reviser import revise
from nodes.formatter import format_letter
from nodes.evaluator import evaluate
from nodes.notifier import notify  # ✅ Real email notifier

# Initialize the graph
graph = StateGraph(SecretaryState)

# Add nodes
graph.add_node("search", search_web)
graph.add_node("weather", check_weather)
graph.add_node("search_reflector", reflect_search)
graph.add_node("timestamp", inject_timestamp)
graph.add_node("generate", generate)
graph.add_node("reflect", reflect)
graph.add_node("revise", revise)
graph.add_node("formatter", format_letter)
graph.add_node("evaluate", evaluate)
graph.add_node("notifier", notify)

# Set entry point
graph.set_entry_point("search")

# Define edges (sequentialized to avoid concurrency)
graph.add_edge("search", "weather")
graph.add_edge("weather", "search_reflector")
graph.add_edge("search_reflector", "timestamp")
graph.add_edge("timestamp", "generate")
graph.add_edge("generate", "reflect")
graph.add_edge("reflect", "revise")
graph.add_edge("revise", "formatter")
graph.add_edge("formatter", "evaluate")
graph.add_edge("evaluate", "notifier")

# Compile the graph
app = graph.compile()