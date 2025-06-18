import os
from dotenv import load_dotenv
import google.generativeai as genai
import chainlit as cl

# 📦 Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 🔐 Configure Gemini API
genai.configure(api_key=gemini_api_key)

# 🤖 Initialize the Gemini AI model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

# 💬 On chat start — Show welcome message
@cl.on_chat_start
async def greeting():
    await cl.Message(
        content=(
            "🧮 **Welcome to Calculator Agent!**\n"
            "You can ask me to solve any math expression like `5 + 3 * 2`\n"
            "✨ This AI Agent is proudly built by **Muzna Zuberi**."
        )
    ).send()

# 💬 On user message — Process and reply
@cl.on_message
async def chat(message: cl.Message):
    prompt = f"Calculator: {message.content}"
    res = model.generate_content(prompt)
    await cl.Message(
        content=f"{res.text}\n\n🛠️ *Powered by Gemini AI | Built by Muzna Zuberi*"
    ).send()
