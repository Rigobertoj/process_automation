from email import message
from multiprocessing import context
import dotenv
import ssl
import email
import smtplib
import csv
from datetime import datetime


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "rigojmtz05@gmail.com"
receiver_email = "rigojmtz05+persona1@gmail.com"

class enviarEmails():

    def __init__(self,
                 sender_email: str,
                 receiver_email: str,
                 password = " ",
                 message = " ",
                 subject = " ",
                 file = " "
                 ):
        self.host = 'smtp.gmail.com'
        self.port = 465
        self.username = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message
        self.file = file
        
    def messageEmail(self, message: str):
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = self.receiver_email
        message["Subject"] = self.subject | " "


    def filñeEmail(self, file: str):
        pass 

        """"""
    def send_email(self):
        contex = ssl-ssl.create_default_context()
        with smtplib.SMTP_SSL(self.host, self.port, context=contex) as server:
            try:
                if(self.password is None):
                    self.password = input("introduce tu contraseña por favor")
                
            except:
                return """
                no se pudo enviar el email
                """