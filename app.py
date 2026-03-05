import streamlit as st
import joblib
import re
import matplotlib.pyplot as plt

# Load saved model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

st.title("Cyber Email Spam Predictor")

st.write("Enter email content below to check if it is Spam or Not Spam.")

email_text = st.text_area("Email Content")

if st.button("Analyze Email"):

    if email_text.strip() == "":
        st.warning("Please enter email content.")
    else:
        cleaned = clean_text(email_text)
        vectorized = vectorizer.transform([cleaned])

        prediction = model.predict(vectorized)[0]
        probability = model.predict_proba(vectorized)[0][1]

        if prediction == 1:
            st.error("⚠ This Email is SPAM")
        else:
            st.success("✅ This Email is NOT Spam")

        st.subheader("Spam Probability")
        st.write(f"{round(probability*100,2)} %")

        # Graph
        fig, ax = plt.subplots()
        ax.bar(["Not Spam", "Spam"], [1-probability, probability])
        st.pyplot(fig)