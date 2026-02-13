import streamlit as st
import openai
import os
from PyPDF2 import PdfReader

# Load API key from Streamlit secrets or environment
openai.api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")

st.set_page_config(page_title="Research Tool - Earnings Call Analyzer")

st.title("📊 Earnings Call Analyzer")
st.write("Upload an earnings call transcript and get structured summary")

uploaded_file = st.file_uploader("Upload transcript (PDF or TXT)", type=["pdf", "txt"])

def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    else:
        text = file.read().decode("utf-8")
    return text

def analyze_transcript(text):
    prompt = f"""
Analyze the following earnings call transcript and provide structured output:

Tone:
Confidence Level:
Key Positives:
Key Concerns:
Future Outlook:

Transcript:
{text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

if uploaded_file is not None:
    if st.button("Analyze"):
        with st.spinner("Analyzing transcript..."):
            text = extract_text(uploaded_file)
            result = analyze_transcript(text)
            st.subheader("Analysis Result")
            st.write(result)
            st.success("Analysis complete!")
