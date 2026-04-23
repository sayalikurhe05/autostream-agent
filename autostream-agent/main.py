import json

# Load knowledge base
with open("data.json", "r") as f:
    data = json.load(f)

# Mock tool
def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")

# Memory (state)
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

# Intent Detection (rule-based)
def detect_intent(user_input):
    text = user_input.lower()

    # ✅ check high intent FIRST
    if any(word in text for word in ["want", "buy", "try", "subscribe", "pro"]):
        return "high_intent"

    elif any(word in text for word in ["price", "plan", "cost"]):
        return "inquiry"

    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "unknown"

# RAG (basic JSON retrieval)
def get_pricing_info():
    response = ""

    for plan in data["plans"]:
        response += f"\n{plan['name']} - {plan['price']}\n"
        for feature in plan["features"]:
            response += f"- {feature}\n"

    return response

# Lead flow
def handle_lead_flow(user_input):

    if state["name"] is None:
        state["name"] = user_input
        return f"Nice to meet you, {state['name']}! Please provide your email."

    elif state["email"] is None:
        state["email"] = user_input
        return "Which platform do you create on? (YouTube/Instagram)"

    elif state["platform"] is None:
        state["platform"] = user_input
        mock_lead_capture(state["name"], state["email"], state["platform"])
        return "✅ Thanks! Your details are submitted successfully."

# MAIN LOOP
print("🤖 AutoStream Agent Started (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Lead flow mode
    if state["intent"] == "high_intent":
        response = handle_lead_flow(user_input)
        print("Bot:", response)
        continue

    # Intent detection
    intent = detect_intent(user_input)
    state["intent"] = intent

    if intent == "greeting":
        print("Bot: Hello! How can I help you today?")

    elif intent == "inquiry":
        print("Bot:", get_pricing_info())

    elif intent == "high_intent":
        print("Bot: Great! Let's get you started. What's your name?")

    else:
        print("Bot: Sorry, I didn’t understand that.")