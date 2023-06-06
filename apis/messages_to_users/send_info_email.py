import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import x

def send_info_email(reciever_email: str, message_plain_text: str, message_html: str) :
    sender_email = "maalmaja@gmail.com"
    reciever_email = reciever_email
    password = "eotfntjhmkiqzjof"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Profile status from twitter"
    message["From"] = sender_email
    message["To"] = reciever_email #hentes fra api_register ved registre

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(message_plain_text, "plain")
    part2 = MIMEText(message_html, "html")

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