# MCQ-generator
LLM MCQ Generator
An AI-powered Multiple Choice Question (MCQ) Generator built using Python, Streamlit, and Hugging Face. The application uses a Large Language Model (LLM) to automatically generate MCQs based on a user-provided topic and selected difficulty level.

Project Overview
The LLM MCQ Generator helps students and educators quickly create practice questions from any given topic.

The user can enter a topic, choose the number of questions, select a difficulty level, and generate MCQs using a Hugging Face language model.

Features
Generate MCQs automatically using an LLM
Enter any educational topic
Select the number of questions
Choose difficulty level:
Easy
Medium
Hard
Generate four options for each question
Display the correct answer
Provide an explanation for each answer
Simple and user-friendly Streamlit interface
Technologies Used
Python
Streamlit
Hugging Face
Hugging Face Inference API
Qwen LLM
python-dotenv
LLM Model
The application uses:

Qwen/Qwen3-32B

The model is accessed through the Hugging Face Inference API.

Streamlit app
https://abcqbmputil4x88uc7revp.streamlit.app/

Project Structure
MCQ_Generator/
│
├── app.py
├── requirements.txt
└── README.md