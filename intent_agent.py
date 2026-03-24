def detect_intent(state):

    text = state["user_input"].lower()

    if "order" in text:
        state["intent"] = "order"

    elif "table" in text or "reserve" in text:
        state["intent"] = "reservation"

    else:
        state["intent"] = "search"

    return state