import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Research Transcript Analyzer")

uploaded_file = st.file_uploader("Upload transcript (.txt)", type=["txt"])

def analyze_transcript(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a research assistant. Analyze transcripts and extract key insights."},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content


if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    if st.button("Analyze"):
        result = analyze_transcript(text)
        st.subheader("Analysis Result")
        st.write(result)
