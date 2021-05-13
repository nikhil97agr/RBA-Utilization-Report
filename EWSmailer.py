from exchangelib import ServiceAccount, Configuration, Account, DELEGATE
from exchangelib import Message, Mailbox, FileAttachment
from cryptography.fernet import Fernet
from configparser import ConfigParser #####load your credentials

def ews_smailer(email,filename):
    def send_email(account, subject, body, recipients, attachments=None):
        to_recipients = []
        for recipient in recipients:
            to_recipients.append(Mailbox(email_address=recipient))
        #####Create message
        m = Message(account=account,
                    folder=account.sent,
                    subject=subject,
                    body=body,
                    to_recipients=to_recipients)

        #####attach files
        for attachment_name, attachment_content in attachments or []:
            file = FileAttachment(name=attachment_name, content=attachment_content)
            m.attach(file)
        m.send_and_save()

    cfg = ConfigParser()
    cfg.read("config.ini")
    credentials = ServiceAccount(username=cfg['mail']['id'],
                                password=cfg['mail']['password'])

    config = Configuration(server="outlook.office365.com", credentials=credentials)
    account = Account(primary_smtp_address=cfg['mail']['id'], config=config,
                    autodiscover=False, access_type=DELEGATE)

    #####Read attachment
    attachments = []
    filename=filename+".xlsx"
    with open(filename, 'rb') as f:
        content = f.read()
    attachments.append((filename, content))

    #####Send email
    body='''Hello,

    Please find attached the utilization report of RBA script of PU DU Account Script name.


    Thank You. 

    Regards
    RBA Utilization Reporter Team


    Incase of any quesries contact us at test.mailclient43@gmail.com
    '''
    subject="RBA Utilization Report - PU DU Account - Script Name"
    send_email(account,subject, body, [email],attachments=attachments)
