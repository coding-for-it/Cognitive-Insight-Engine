import streamlit as st
import requests

st.title("📊 Cognitive Insight Engine")

uploaded_file = st.file_uploader("Upload Annual Report (PDF or Excel)", type=["pdf", "xlsx"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    files = {"file": (uploaded_file.name, uploaded_file, f"application/{file_type}")}

    response = requests.post("http://localhost:8000/upload/", files=files)

    if response.ok:
        data = response.json()

        st.subheader("Extracted KPIs")
        st.json(data["kpis"])

        st.subheader("Sentiment Analysis")
        st.json(data["sentiment"])

        st.subheader("Sections Found")
        st.write(data["sections"])

        # 🎯 Conclusion block
        st.subheader("🧠 Insight Conclusion")
        polarity = data['sentiment']['polarity']
        if polarity > 0.2:
            st.success("Overall positive tone in the report. Financial outlook appears optimistic.")
        elif polarity < -0.2:
            st.error("Report indicates concerns or negative tone. Possible financial or strategic risks.")
        else:
            st.info("Neutral or mixed sentiment. No strong emotional tone detected.")
    else:
        st.error("Failed to extract data. Please try again.")
