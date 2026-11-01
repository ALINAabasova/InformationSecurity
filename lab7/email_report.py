#!/usr/bin/env python3
import smtplib
import datetime
import shutil
from email.mime.text import MIMEText

sender = "youremail@gmail.com"
app_password = "YOUR_APP_PASSWORD"
owner = "youremail@gmail.com"

total, used, free = shutil.disk_usage("/")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text = f"Server report {now}\nFree disk: {free // (1024**3)} GB"

msg = MIMEText(text)
msg["Subject"] = "Server status report"
msg["From"] = sender
msg["To"] = owner

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, app_password)
    server.send_message(msg)
print("Report email sent.")
