from groq_agent import priya_chat

def chat_node(state):

    response = priya_chat(
        state["user_input"],
        state["context"]
    )

    state["response"] = response

    return state