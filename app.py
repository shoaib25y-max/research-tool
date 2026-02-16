import streamlit as st
from openai import OpenAI

# This pulls the key from the Secrets you just saved
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_transcript(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
        temperature=0.3
    )
    return response
