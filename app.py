import streamlit as st
import requests

def upload_resume(file):
    url = "http://127.0.0.1:8000/upload_resume"  # Update if FastAPI is running elsewhere
    files = {"file": file}
    response = requests.post(url, files=files)
    return response.json()

st.title("AI-Powered Resume Parser")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing..."):
        result = upload_resume(uploaded_file)
        st.success("Parsing Complete!")
        st.json(result)
