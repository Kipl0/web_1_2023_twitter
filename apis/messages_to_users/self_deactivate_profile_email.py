import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import x

def deactivate_own_profile(deactivate_key,reciever_email) :

    sender_email = "maalmaja@gmail.com"
    reciever_email = reciever_email
    password = "eotfntjhmkiqzjof"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Confirm deactivate your profile"
    message["From"] = sender_email
    message["To"] = reciever_email #hentes fra api_register ved registre

    # print("hello")

    text = f"""\
        Hi!
        To deactivate your profile click the link below <br>
        Deactivate profile--> https://kipl0.eu.pythonanywhere.com/self-deactivate-profile/{deactivate_key}
    """
    html = f"""\
    <html>
        <body>
            <h2>Hi!</h2>
            <p>To deactivate your profile click the link below</p>
            <p>Click this link to --> <a href="https://kipl0.eu.pythonanywhere.com/self-deactivate-profile/{deactivate_key}">deactivate profile!</a></p>
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