import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser

def send_test_email():
    config = ConfigParser()
    config.read("config.ini")

    sender_email = config.get("Email", "sender_email")
    receiver_email = config.get("Email", "receiver_email")
    password = config.get("Email", "password")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "Just a test email."
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email: ", e)

if __name__ == "__main__":
    send_test_email()
