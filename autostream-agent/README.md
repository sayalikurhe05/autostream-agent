🔹 Project Title

Social-to-Lead Agentic Workflow (AutoStream)

🔹 How to Run
Clone the repository

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py
🔹 Architecture

This project implements a conversational AI agent for a SaaS product (AutoStream) that converts user conversations into potential leads.

The system uses a rule-based intent classification approach to identify whether the user is greeting, asking about pricing, or showing high intent to sign up.

A simple RAG (Retrieval Augmented Generation) mechanism is implemented using a local JSON file that stores pricing and policy data. The agent retrieves relevant information from this knowledge base to answer user queries.

The application maintains state using an in-memory dictionary, which allows it to remember user inputs across multiple conversation turns (name, email, platform).

When a high-intent user is detected, the agent triggers a lead capture workflow, collecting user details step-by-step. After gathering all required information, a mock API function is executed to simulate lead storage.

This design demonstrates a basic agentic workflow, combining intent detection, retrieval, memory, and tool execution.

🔹 WhatsApp Integration (Webhooks)

To integrate this system with WhatsApp, the following approach can be used:

Use WhatsApp Cloud API
Configure a Webhook endpoint on the backend
When a user sends a message:
WhatsApp forwards it to the webhook
Backend sends the message to the agent
Agent processes it (intent + retrieval + logic)
Response is sent back via WhatsApp API

This enables real-time conversational interaction with users on WhatsApp.

🔹 Features
Intent detection (greeting, inquiry, high-intent)
RAG using local knowledge base (JSON)
Multi-turn conversation with memory (state management)
Lead capture workflow
Conditional tool execution (mock API)