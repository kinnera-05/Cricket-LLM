import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_response(question):
    """Get the model response for a given question."""
    prompt = (
        f"Please analyze the question and follow these rules:\n"
        f"1. If the question asks for IPL data beyond 2024, respond with: "
        f"'Sorry, I don't have data beyond 2024. We are working on it. We'll update it soon :)'\n"
        f"2. If the question is about cricket but not IPL for data beyond 2022, respond with: "
        f"'The question is not related to IPL. Please ask a question related to IPL as it is greater than 2022 :)'\n"
        f"3. Otherwise, provide an accurate IPL-related response.\n\n"
        f"Question: {question}"
    )
    
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Cricket Q&A", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Q&A Application")
question = st.text_input("Please ask a question related to Cricket:")
if st.button("Get Answer"):
    if question:
        response_text = get_response(question)
        st.write(response_text)
    else:
        st.error("Please enter a question.")
