import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        r"\b(hi|hello|hey|1)\b": "Hello! Welcome to our grocery store. How can I assist you today?",
        r"\bhow are you\b|\b2\b": "I'm just a bot, but I'm functioning great! How can I help you?",
        r"\b(order status|track order|3)\b": "Sure! Please provide your order ID so I can check its status.",
        r"\b(shipping time|delivery time|4)\b": "We offer same-day delivery and standard 3–5 day shipping.",
        r"\b(return policy|returns|5)\b": "You can return unopened items within 7 days of purchase.",
        r"\b(thank you|thanks|6)\b": "You're welcome! Let me know if there's anything else I can do.",
        r"\b(price|cost|7)\b": "Please mention the product name to check its price.",
        r"\bmilk|8\b": "Milk is ₹30 per liter.",
        r"\beggs|9\b": "A dozen eggs cost ₹80.",
        r"\brice|10\b": "Rice is ₹50 per kilogram.",
        r"\b(vegetables|veggies|11)\b": "We have fresh carrots, potatoes, spinach, and more. What are you looking for?",
        r"\bfruits|12\b": "We currently have apples, bananas, and oranges in stock.",
        r"\bsnacks|13\b": "We offer chips, biscuits, and chocolates. Would you like something specific?",
        r"\b(beverages|drinks|14)\b": "We carry juices, soft drinks, and bottled water.",
        r"\b(buy|order|15)\b": "You can place an order on our website or visit our physical store.",
        r"\b(payment methods|payment|16)\b": "We accept cash, credit/debit cards, and UPI.",
        r"\b(store hours|timing|17)\b": "Our store is open daily from 8 AM to 10 PM.",
        r"\b(location|address|18)\b": "We are located at XYZ Market, Main Street, YourCity.",
        r"\b(bye|exit|19)\b": "Goodbye! Have a great day shopping!"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't quite get that. Could you ask about a specific item or topic?"

# Chatbot interaction loop
def main():
    print("Welcome to our Grocery Chatbot! Type 'exit' or 'bye' to end the conversation.")

    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day shopping!")
            break
        response = chatbot_response(user_message)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
