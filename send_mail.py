from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv
from dotenv import load_dotenv


def send_email(message):
    load_dotenv()
    mail_addr = "blushedn@gmail.com"
    with SMTP_SSL("smtp.gmail.com", 
                  context=create_default_context()) as server:
        server.login(mail_addr, getenv("pypass"))
        server.sendmail(mail_addr, mail_addr, message)