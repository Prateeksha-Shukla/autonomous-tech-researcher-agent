import streamlit as st
import subprocess

st.title("Autonomous Technology Researcher Agent")

topic = st.text_input("Enter Technology Topic")

if st.button("Run Research"):
    subprocess.run(["python", "main.py"])
