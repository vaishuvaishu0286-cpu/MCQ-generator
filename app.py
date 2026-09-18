import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Hugging Face token
HF_TOKEN = os.getenv("HF_TOKEN")

# Hugging Face model
MODEL = "Qwen/Qwen3-32B"

client = InferenceClient(
    model=MODEL,
    provider="nscale",
    token=HF_TOKEN
)

# Page settings
st.set_page_config(
    page_title="MCQ Generator",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("MCQ Generator")
st.write("Generate multiple-choice questions using an LLM.")

# User inputs
topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Python Programming"
)

number = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Generate button
if st.button("Generate MCQs"):

    if not topic:
        st.warning("Please enter a topic.")

    elif not HF_TOKEN:
        st.error("Hugging Face token not found. Check your .env file.")

    else:
        prompt = f"""
Generate {number} multiple-choice questions about {topic}.

Difficulty level: {difficulty}

For each question provide:

Question:
A.
B.
C.
D.
Correct Answer:
Explanation:

Make sure there are exactly four options for every question.
Do not repeat questions.
"""

        with st.spinner("Generating MCQs..."):

            try:
                response = client.chat_completion(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an educational MCQ generator."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=2000,
                    temperature=0.7
                )

                result = response.choices[0].message.content

                st.success("MCQs generated successfully!")

                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")