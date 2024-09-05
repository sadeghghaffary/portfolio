import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email=st.text_input(label="",placeholder="your email adress", key="text_input")
    message=st.text_area(label="",placeholder="your message", key="text_area")
    message=user_email+"\n"+message
    button=st.form_submit_button("Submit")
    if button:
        send_email(message)

