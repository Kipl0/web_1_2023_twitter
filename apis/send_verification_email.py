# "user_verification_key" : str(uuid.uuid4()).replace("-", ""),

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import x

def send_verification_email(reciever_email,verification_key) :

    sender_email = "maalmaja@gmail.com"
    # reciever_email = "maalmaja@gmail.com"
    password = "eotfntjhmkiqzjof"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = reciever_email #hentes fra api_register ved registre

    print(verification_key)

    text = f"""\
        Hi!
        Welcome to Twitter <br>
        You must verify your email before logging in. <br>
        Click this link to --> https://kipl0.eu.pythonanywhere.com/verify-email/{verification_key}
    """
    html = f"""\
    <html>
        <body>
            <p> Hi! <br>
            Welcome to Twitter <br>
            You must verify your email before logging in. <br>
            Click this link to --> <a href="https://kipl0.eu.pythonanywhere.com/verify-email/{verification_key}">verify email!</a>
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