from langgraph.graph import StateGraph
from state import SecretaryState

# Import all agent nodes
from nodes.search import search_web
from nodes.weather import check_weather
from nodes.generator import generate
from nodes.reflector import reflect
from nodes.reviser import revise
from nodes.evaluator import evaluate
from nodes.search_reflector import reflect_search

# Initialize the graph with your shared state class
graph = StateGraph(SecretaryState)

# Add nodes
graph.add_node("search", search_web)
graph.add_node("weather", check_weather)
graph.add_node("search_reflector", reflect_search)
graph.add_node("generate", generate)
graph.add_node("reflect", reflect)
graph.add_node("revise", revise)
graph.add_node("evaluate", evaluate)

# Set entry point
graph.set_entry_point("search")

# Define edges (execution flow)
graph.add_edge("search", "weather")
graph.add_edge("weather", "search_reflector")       # ✅ Sequentialized to avoid concurrency
graph.add_edge("search_reflector", "generate")
graph.add_edge("generate", "reflect")
graph.add_edge("reflect", "revise")
graph.add_edge("revise", "evaluate")

# Compile the graph
app = graph.compile()