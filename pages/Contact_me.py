import streamlit as st
import send_mail

st.title('Contact me')

# Set contact form
with st.form('contact', True):
    contact_email = st.text_input(':email:', placeholder='Enter your email...', key='email')
    contact_message = st.text_area(':pencil2:', placeholder='Write your message...', height=200, key='message')
    message = f"Subject: ShowcaseWeb message\n\nFrom: {contact_email}\n\n{contact_message}"
    button = st.form_submit_button('Send message')
    if button:
        #Send email when user press "send message" button
        send_mail.send_email(message)
        st.info("Your message has been sent succesfully!")