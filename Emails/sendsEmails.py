import dotenv
from data_validate import processValidator
from classSend import enviarEmails

path_file_excel = "C:/Users/Promotora/rigoberto/python/process_automation/Emails/clients/clients.xlsx"
config = dotenv.dotenv_values("../env/.env")

class EnviarEmails():
    def __init__(self, sender_email: str, password_email: str,path_file :str, sheet_name:str ,asunto = " ", mensaje =" ", path_excel_doc = " "):
        self.sendMails = enviarEmails(sender_email=sender_email, password_email=password_email, receiver_email=" ")
        excel_doc = processValidator(file_path=path_file, sheet_name=sheet_name)
        
        print(excel_doc.current_date)
        data = excel_doc.get_validation()
        self.data = data 
        self.sender_email = sender_email
        self.password = password_email


    def set_message_html(self,message: str):
        self.sendMails.messageEmail(message, "html")


    def set_message_text(self, message: str):
        self.sendMails.messageEmail(message, "plain")


    def send(self):
        # for client in self.data["correos"]:

        print(self.data)
        


if __name__ == "__main__":
    print(config.keys)