import streamlit as st
import csv
import smtplib, ssl

with open('C:/Users/Elara/Documents/pass.txt', 'r') as file:
    password_file = file.read()


def send_email(message):  # I had to put the code here cuz wasn't importing
    host = 'smtp.gmail.com'
    port = 465
    username = 'elaramendes39@gmail.com'
    password = password_file
    receiver = 'elaramendes39@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


with open('60-days-learning-python/day-22/topics.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    topics = [row[0] for row in reader]  # Revisit

st.header('Contact Us')

with st.form(key='my_form'):
    sender = st.text_input('Write your email:')
    topic_selected = st.selectbox('Topics:', topics)
    message_raw = st.text_area('Message:')
    message = f"""\
    Subject: {topic_selected}
    \n
    From: {sender}
    \n
    Message: {message_raw}
"""
    button = st.form_submit_button('Send')
    if button:
        send_email(message)
        st.info('Email sent successfully!')

