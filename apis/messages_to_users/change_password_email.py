# "user_verification_key" : str(uuid.uuid4()).replace("-", ""),

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import x

def send_change_password_email(reciever_email,change_key) :

    sender_email = "maalmaja@gmail.com"
    reciever_email = reciever_email
    password = "eotfntjhmkiqzjof"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = reciever_email #hentes fra api_register ved registre

    # print("hello")

    text = f"""\
        Hi!
        To reset your password click the link below <br>
        Click this link to reset password --> https://kipl0.eu.pythonanywhere.com/change-password/{change_key}
    """
    html = f"""\
    <html>
        <body>
            <h2>Hi!</h2>
            <p>To reset your password click the link below </p>
            <p>Click this link to reset password --> <a href="https://kipl0.eu.pythonanywhere.com/change-password/{change_key}">reset password!</a></p>
            </p>
        </body>
    </html>
    """


    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, reciever_email, message.as_string()
        )