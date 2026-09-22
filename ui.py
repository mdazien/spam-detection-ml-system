import streamlit as st
import requests

st.title("📩 Spam Detection System")

msg = st.text_area("Enter message")

if st.button("Check"):
    if msg.strip():
        res = requests.post(
            "https://spam-detection-api-cpzy.onrender.com/predict",
            json={"message": msg}
        )

        if res.status_code == 200:
            data = res.json()

            st.subheader("Result")
            st.write("Prediction:", data["prediction"])
            st.write("Spam %:", data["spam_probability"])
            st.write("Confidence:", data["confidence"])
            st.write("Risk Words:", data["risk_factors"])

            st.progress(data["spam_probability"]/100)

        else:
            st.error("API error")
    else:
        st.warning("Enter text")

""" UPGRADE THE UI """