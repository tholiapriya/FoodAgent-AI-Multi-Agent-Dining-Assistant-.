from graph import graph
from payment_qr import generate_qr
from agents.payment_agent import make_payment

print("\n🤖 FoodAgent AI Assistant\n")

order_pending = False

while True:

    user_input = input("Customer: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("FoodAgent: Goodbye!")
        break

    # If payment pending
    if order_pending and user_input.lower() == "paid":

        payment = make_payment(450)

        print("\nFoodAgent:", payment, "\n")

        order_pending = False
        continue


    state = {
        "user_input": user_input,
        "intent": "",
        "context": "",
        "response": ""
    }

    result = graph.invoke(state)

    response = result["response"]

    print("\nFoodAgent:", response, "\n")

    # If order confirmed → show QR
    if "Order confirmed" in response:

        payment_link = "https://dummy-pay.com/foodagent"

        generate_qr(payment_link)

        print("\nFoodAgent: Scan the QR code to complete payment.")
        print("FoodAgent: Type 'paid' after payment.\n")

        order_pending = True