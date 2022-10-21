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
    """
    attributes : 
        host (srt) : 'smtp.gmail.com' host intermediario entre el emisor y receptor
        port (int) : 465 puerto al cual nos conectamos por defecto en el localhost
        username (str) : emisor del email
        password (str) : password del emisor
        receiver_email (str) : "quien recibe el email"
        subject (str) : asunto del email - no obligatorio
        message (str) : mensaje que se pretende enviar - no obligatorio 
        file (doc) : documento que se pretende enviar - no obligatorio

    clase: 
        nos permite emitir un emeil de manera automatica a n cantidad de receptores
    """
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
        """
        params: 
            message (str) : mensaje que se pretende enviar, puede ser de tipo plano o html
            type (str) : formato que se le dara al mensaje si plano o html
            alternative_message (str) :  mismo que el mensaje en formato plano - opccional
            subject (str) : asunto del email - opccional
        
        metod:
            nos permite agregar uno o mas mensaje, este pude ser en html o plano especificado en el parametro type, con opccion a agregar el asunto y un mensaje alternativo con el mismo contenido que el principal solo que en texto plano \n

            si se pretende agregar otro mensaje se hace otra llamda al metodo y se define lo antes mencionado
        
        """
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
        """ 
        params: 
            path_file (str) : ruta donde se encuentra el archivo, 
            type_file (str) : typo de documento que se anexa

        metod:
            nos permite agregar un o mas documentos al correo para cada doc se hace una llamada al metodo y se agrega el siguiente doc
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
        """
        metod: 
            nos permite enviar el correo que ya se preestablecido y definido todas sus partes
        """

        context = ssl.create_default_context()
    # smtplib.SMTP_SSL("smtp.gmail.com", port=465, contex) protocolo de mensajeria segura que nos permitira realizar operaciones con nuestros emails

        with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
            try:

        # .login(email, clave_de_aut) -> clave_de_aut es la clave que otorga google cuanddo se quiere autenticar con otra app menos segura
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
        """
        param: 
            receiver_email (str) : receptor del email

        metod:
            establece quien sera el receptor del email 
        """
        self.receiver_email = receiver_email


if __name__ == "__main__":
    estados_cuenta = enviarEmails(
        sender_email=sender_email, receiver_email=receiver_email, password=password_email,)
    estados_cuenta.messageEmail(HTML, "html", subject="Estados cuenta con las class")
    estados_cuenta.add_fileEmail("./MX-M565N_20220927_141858.pdf","rb")
    estados_cuenta.send_email()
