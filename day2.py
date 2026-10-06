from groq import Groq
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

print("API key loaded successfully!")

# Create Groq client
client = Groq(api_key=api_key)

# Chat history
chat_history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant.Explain things in simple language"
    }
]
print("\n Groq AI Chatbot🤖")
print("type exit to stop the chatbot.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot : Goodbye👋")
        break

    # Add user message to chat history
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Send complete chat history to Groq
    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=chat_history
)


    assistant_reply = response.choices[0].message.content

    print("AI:", assistant_reply)

    # Add AI response to chat history
    chat_history.append({
        "role": "assistant",
        "content": assistant_reply
    })