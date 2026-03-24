from agents.reservation_agent import reserve_table

def reservation_node(state):

    reservation = reserve_table(2)

    state["response"] = reservation

    return state