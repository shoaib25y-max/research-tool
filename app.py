import streamlit as st
from openai import OpenAI

# Read API key from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Research Transcript Analyzer")

uploaded_file = st.file_uploader("Upload transcript", type=["txt"])

def analyze_transcript(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a research assistant."},
            {"role": "user", "content": f"Analyze this transcript:\n{text}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    if st.button("Analyze"):
        result = analyze_transcript(text)
        st.write(result)
