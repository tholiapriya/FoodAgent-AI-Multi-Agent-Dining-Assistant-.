from restaurant_search import get_restaurant_context

def search_restaurant(state):

    query = state["user_input"]

    context = get_restaurant_context(query)

    state["context"] = context

    return state