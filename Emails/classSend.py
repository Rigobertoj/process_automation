from email import message
from multiprocessing import context
import dotenv
import ssl
import email
import smtplib
from datetime import datetime
from formatEstadoCuenta import HTML

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = dotenv.dotenv_values("../env/.env")

M = "test class enviarEmails()"

sender_email = "rigojmtz05@gmail.com"
receiver_email = "rigojmtz05+persona1@gmail.com"
password_email = config["KEY_lOGING_P"]


class enviarEmails():

    def __init__(self,
                 sender_email: str,
                 receiver_email: str,
                 password=" ",
                 message=" ",
                 subject=" ",
                 file=" "
                 ):
        # instanacia MIMEMultipart que genera un mensaje tipo email
        self.host = 'smtp.gmail.com'
        self.port = 465
        self.username = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message
        self.file = file

    def messageEmail(self, message: str, type: str, alternative_message=" ",  subject=" "):
        """metodo que nos ayuda a agregar un mensaje, el asunto y un mensaje alternativo en texto plano """
        MIMEmessage = MIMEMultipart("alternative")

        # declarando el emeiso y receptor del email
        MIMEmessage["From"] = self.username
        MIMEmessage["To"] = self.receiver_email

        # si existe el asunto se asigna
        if (self.subject != " "):
            MIMEmessage["Subject"] = self.subject

        # si self.subject no exite y el arg asunto existe se asigna
        MIMEmessage["Subject"] = subject
        self.subject = subject
        print(self.subject)

        
        # instancia del texto del email con el mensaje y el formato o type
        message_body = MIMEText(message, type)
        MIMEmessage.attach(message_body)

        # si hay un mensaje alternativo se agrega al texto
        if (alternative_message != " "):
            message_body_2 = MIMEText(alternative_message, "plain")
            MIMEmessage.attach(message_body_2)

        # MIMEmessage.as_string()
        self.MIMEmessage = MIMEmessage

    def add_fileEmail(self, path_file: str, type_file: str):
        """ metodo que nos permite agregar un o mas doc o archivo al correo
    para cada doc se hace una llamada al metodo y se agrega el siguiente doc
        """

        # abrimos el doc
        with open(path_file, type_file) as file:
            print("entra")
            part = MIMEBase("Application", "octet-stream")
            part.set_payload(file.read())

        encoders.encode_base64(part)

        part.add_header("content-disposition",
                        f"attachment; filename={path_file}")
        self.MIMEmessage.attach(part)

    # TODO: crear un metodo que nos permita agregar otra párte al correo
    def add_part_message(self):
        pass

        """"""

    def send_email(self):
        context = ssl.create_default_context()
    # smtplib.SMTP_SSL("smtp.gmail.com", port=465, contex) protocolo de mensajeria segura que nos permitira realizar operaciones con nuestros emails
        with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
            try:
        # .login(email, clave_de_auto) -> clave_de_auto es la clave que otorga google cuanddo se quiere autenticar con otra app menos segura
                server.login(self.username, self.password)
        # .sendmail(email_emisor, email_receptor, The_message )
                server.sendmail(
                    self.username,
                    self.receiver_email,
                    self.MIMEmessage.as_string()
            )
            except:
                return False


    def set_receiver_email(self, receiver_email: str):
        self.receiver_email = receiver_email


if __name__ == "__main__":
    estados_cuenta = enviarEmails(
        sender_email=sender_email, receiver_email=receiver_email, password=password_email,)
    estados_cuenta.messageEmail(HTML, "html", subject="Estados cuenta con las class")
    estados_cuenta.add_fileEmail("./MX-M565N_20220927_141858.pdf","rb")
    estados_cuenta.send_email()
