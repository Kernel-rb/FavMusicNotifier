import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser
import keyboard
import time
import sys

def send_error_email(error_message):
    config = ConfigParser()
    config.read("config.ini")

    sender_email = config.get("email", "sender_email")
    receiver_email = config.get("email", "receiver_email")
    password = config.get("email", "password")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Error occurred while playing music"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"An error occurred:\n{error_message}"
    html = f"""\
    <html>
        <body>
            <p>An error occurred:</p>
            <p>{error_message}</p>
        </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def skip_song():
    keyboard.press_and_release('ctrl+right')

def skip_10s():
    keyboard.press_and_release('right')

def animate(term):
    while done == 'false':
        sys.stdout.write(f'\r{term} |')
        time.sleep(0.1)
        sys.stdout.write(f'\r{term} /')
        time.sleep(0.1)
        sys.stdout.write(f'\r{term} -')
        time.sleep(0.1)
        sys.stdout.write(f'\r{term} \\')
        time.sleep(0.1)

    sys.stdout.write(f'\rDone!     ')

playlist = [
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\Baghi nchoufa.mp3",
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\bghit_nkhtiha.mp3",
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\Halfa nougda.mp3",
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\MonCoeur.mp3",
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\Sadek_lw9t_rah.mp3",
    "C:\\Users\\petmk\\Desktop\\fav_music\\playlist\\3ch9na_khatar.mp3",
]

for music in playlist:
    try:
        done = 'false'  # Reset done before each iteration
        os.startfile(music)
        print("Playing:", music.split("\\")[-1])
        animate("Listening")  # Call the animation function with the term "Listening"
        keyboard.wait('ctrl+*')
    except Exception as e:
        print(e)
        send_error_email(str(e))
    finally:
        done = 'true'  # Set done to true when the animation is complete
        keyboard.unhook_all()
