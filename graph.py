from langgraph.graph import StateGraph
from state import RestaurantState

from intent_agent import detect_intent
from search_node import search_restaurant
from order_node import order_node
from reservation_node import reservation_node
from chat_node import chat_node

builder = StateGraph(RestaurantState)

builder.add_node("intent", detect_intent)
builder.add_node("search", search_restaurant)
builder.add_node("order", order_node)
builder.add_node("reservation", reservation_node)
builder.add_node("chat", chat_node)

builder.set_entry_point("intent")


def route(state):

    if state["intent"] == "order":
        return "order"

    elif state["intent"] == "reservation":
        return "reservation"

    else:
        return "search"


builder.add_conditional_edges(
    "intent",
    route,
    {
        "order": "order",
        "reservation": "reservation",
        "search": "search"
    },
)

builder.add_edge("search", "chat")

graph = builder.compile()