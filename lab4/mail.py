import os
import smtplib
from email.mime.text import MIMEText

sender = os.environ["SENDER_EMAIL"]
password = os.environ["SENDER_APP_PASSWORD"]
recipient = os.environ["RECIPIENT_EMAIL"]

message = MIMEText(
    """This is an educational phishing-awareness exercise.

A local demonstration application is available at:
http://127.0.0.1:8000

This address works only on the computer running the application.
Do not enter real payment information.
"""
)

message["Subject"] = "Phishing Awareness Training Demo"
message["From"] = sender
message["To"] = recipient

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(message)

print("Training email sent successfully.")