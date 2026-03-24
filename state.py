from typing import TypedDict

class RestaurantState(TypedDict):
    user_input: str
    intent: str
    context: str
    response: str