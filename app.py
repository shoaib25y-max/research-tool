import streamlit as st
from openai import OpenAI

# Correct way to load API key from Streamlit Secrets
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
)

st.title("📊 Earnings Call Analyzer")

uploaded_file = st.file_uploader("Upload transcript (.txt)", type=["txt"])

def analyze_transcript(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": f"Analyze this transcript and give Tone, Confidence Level, Key Positives, Key Concerns, Future Outlook:\n\n{text}"}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


if uploaded_file is not None:

    text = uploaded_file.read().decode("utf-8")

    if st.button("Analyze"):

        with st.spinner("Analyzing..."):

            result = analyze_transcript(text)

            st.subheader("Analysis Result")

            st.write(result)

            st.success("Done!")

