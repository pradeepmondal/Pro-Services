import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "localhost"
SMTP_PORT = "1025"
SENDER_EMAIL = "support@proservices.xyz"
SENDER_PASSWORD = ""

def send_email(to, subject, content):

    message = MIMEMultipart()
    message['To'] = to
    message['Subject'] = subject
    message['From'] = SENDER_EMAIL

    message.attach(MIMEText(content,'html'))

    client = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
    client.send_message(message)
    client.quit()
    

# send_email(to="krish02@example.com", subject="Reminder", content="<h1> Today's Reminders</h1>")
