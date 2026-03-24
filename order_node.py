from agents.order_agent import place_order

def order_node(state):

    dish = "Special Thali"

    if "biryani" in state["user_input"].lower():
        dish = "Chicken Biryani"

    order = place_order(dish, "The Local Kitchen")

    state["response"] = order

    return state