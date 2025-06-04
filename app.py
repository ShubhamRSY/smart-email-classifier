import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# App Title
st.title("📬 Smart Email Classifier")
st.write("Classify or summarize SMS messages using GPT")

# User Input
input_msg = st.text_area("📨 Enter your SMS message here:")

# Task Selection
task = st.selectbox("🔍 Choose Task", ["Few-Shot Classification", "Zero-Shot Summarization", "Chain-of-Thought Reasoning"])

# Run button
if st.button("Run") and input_msg.strip() != "":
    if task == "Few-Shot Classification":
        prompt = f"""
Classify the following message as Spam or Not Spam:

Message 1: "Free entry in 2 a wkly comp to win FA Cup final tkts! Text FA to 87121 to receive entry code."
Label: Spam

Message 2: "Hey, are we still meeting for lunch today at 1 PM? Let me know."
Label: Not Spam

Message 3: "{input_msg}"
Label:
"""
    elif task == "Zero-Shot Summarization":
        prompt = f"""Summarize this SMS in one sentence:\n\n"{input_msg}"\n"""
    else:  # Chain-of-Thought
        prompt = f"""
You are an expert in detecting spam messages. Given an SMS message, explain your reasoning step-by-step and then clearly state whether it's Spam or Not Spam.

Message: "{input_msg}"

Reasoning and Final Label:
"""

    # Call GPT
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        output = response.choices[0].message.content.strip()

    # Display result
    st.subheader("🤖 GPT Response")
    st.write(output)
