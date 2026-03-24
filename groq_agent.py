from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation memory
messages = [
    {
        "role": "system",
        "content": """
You are Priya, a helpful restaurant assistant.

Your job is to help customers find restaurants, choose dishes, reserve tables, or place orders.

Rules:
- Keep responses short (1–2 sentences only).
- Do not repeat greetings.
- Do not restart the conversation.
- Use the restaurant information provided.
- If a user selects a restaurant, ask the next step (menu, order, or reservation).
- Be clear and direct.
"""
    }
]


def priya_chat(user_input, context):

    global messages

    # Create prompt with restaurant context
    prompt = f"""
Restaurant information:
{context}

Customer message:
{user_input}
"""

    # Add user message to memory
    messages.append({"role": "user", "content": prompt})

    try:
        # Call Groq model
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.4,
            max_tokens=80
        )

        reply = response.choices[0].message.content

        # Save assistant response to memory
        messages.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return f"I'm having trouble connecting right now. (Error: {e})"