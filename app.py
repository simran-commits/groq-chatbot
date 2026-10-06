from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=api_key)

# Page settings
st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Groq AI Chatbot")
st.write("Ask me anything!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Explain things in simple language."
        }
    ]

# Display previous messages
for message in st.session_state.chat_history:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Add user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=st.session_state.chat_history
    )

    assistant_reply = response.choices[0].message.content

    # Display AI response
    with st.chat_message("assistant"):
        st.write(assistant_reply)

    # Add AI response to history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_reply
    })
