import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser

def send_test_email():
    config = ConfigParser()
    config.read("config.ini")

    # Affiche le contenu du fichier config.ini
    print("Contenu de config.ini :")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")

    sender_email = config.get("Email", "sender_email")
    receiver_email = config.get("Email", "receiver_email")
    password = config.get("Email", "password")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "Ceci est un email de test pour vérifier si la configuration SMTP fonctionne."
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:
        # Utilisez SMTP_SSL pour une connexion sécurisée
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email de test envoyé avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email de test :", e)

if __name__ == "__main__":
    send_test_email()
