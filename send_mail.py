from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv
from dotenv import load_dotenv


load_dotenv()

def send_email(message:str, mail_addr=getenv("email"), mail_pass=getenv("pypass")):
    """Sends an email with the given message to the given email in .env

    Args:
        message (str): E-mail message (body)
        mail_addr (_type_, optional): E-mail address. Defaults to getenv("email").
        mail_pass (_type_, optional): E-mail password. Defaults to getenv("pypass").
    """
    with SMTP_SSL("smtp.gmail.com", 
                  context=create_default_context()) as server:
        server.login(mail_addr, mail_pass)
        server.sendmail(mail_addr, mail_addr, message)