import smtplib, ssl

with open('C:/Users/Elara/Documents/pass.txt', 'r') as file:
    password_file = file.read()


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'elaramendes39@gmail.com'
    password = password_file
    receiver = 'elaramendes39@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
