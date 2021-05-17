from exchangelib import ServiceAccount, Configuration, Account, DELEGATE
from exchangelib import Message, Mailbox, FileAttachment
from cryptography.fernet import Fernet
from configparser import ConfigParser 
import logging

##### funtion for sending report on email to entered email address #####
def ews_smailer(email,filename,list):
    def send_email(account, subject, body, recipients, attachments=None):
        to_recipients = []
        for recipient in recipients:
            to_recipients.append(Mailbox(email_address=recipient))
        #####Create message#####
        m = Message(account=account,folder=account.sent,subject=subject,body=body,to_recipients=to_recipients)

        #####attach files#####
        for attachment_name, attachment_content in attachments or []:
            file = FileAttachment(name=attachment_name, content=attachment_content)
            m.attach(file)
        m.send_and_save()
        logger.info("Email sent successfully")
    ##### Create and configure logger #####
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    ##### Creating an object #####
    logger=logging.getLogger()
  
    ##### Setting the threshold of logger to DEBUG #####
    logger.setLevel(logging.DEBUG)
    logger.info("Function for sending email is called")

    cfg = ConfigParser()
    cfg.read("config.ini")
    key=cfg['mail']['key']
    key=bytes(key, 'utf-8')
    print(type(key))
    passw=bytes(cfg['mail']['password'],'utf-8')
    f= Fernet(key)
    print(f.decrypt(cfg['mail']['password']).decode("utf-8"))
    credentials = ServiceAccount(username=cfg['mail']['id'],password=f.decrypt(passw).decode("utf-8"))

    config = Configuration(server="outlook.office365.com", credentials=credentials)
    account = Account(primary_smtp_address=cfg['mail']['id'], config=config,autodiscover=False, access_type=DELEGATE)

    #####Read attachment#####
    attachments = []
    filename=filename+".xlsx"
    with open(filename, 'rb') as f:
        content = f.read()
    attachments.append((filename, content))

    #####Send email#####
    body='''
Hello,

Please find attached the utilization report of RBA script of\n
    PU : '''+list[0]+'''
    DU : '''+list[1]+'''
    Account : '''+list[2]+'''
    Script name. : '''+filename+'''


Thank You. 

Regards
RBA Utilization Reporter Team


Incase of any quesries contact us at xxyyzz@gmail.com
    '''
    subject="RBA Utilization Report - "+list[0]+"-"+list[1]+"-"+list[2]+"-"+filename
    send_email(account,subject, body, [email],attachments=attachments)

##### Function for error reporting to internal team #####
def ews_smailer_error(subject,body):
    def send_email(account, subject, body, recipients, attachments=None):
        to_recipients = []
        for recipient in recipients:
            to_recipients.append(Mailbox(email_address=recipient))
        #####Create message#####
        m = Message(account=account,folder=account.sent,subject=subject,body=body,to_recipients=to_recipients)

        #####attach files#####
        for attachment_name, attachment_content in attachments or []:
            file = FileAttachment(name=attachment_name, content=attachment_content)
            m.attach(file)
        m.send_and_save()
        logger.info("Email sent successfully")
    ##### Create and configure logger #####
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    ##### Creating an object #####
    logger=logging.getLogger()
  
    ##### Setting the threshold of logger to DEBUG #####
    logger.setLevel(logging.DEBUG)
    logger.info("Function for sending email for error reporting is called")

    cfg = ConfigParser()
    cfg.read("config.ini")
    key=cfg['mail']['key']
    key=bytes(key, 'utf-8')
    passw=bytes(cfg['mail']['password'],'utf-8')
    print(type(key))
    f= Fernet(key)
    credentials = ServiceAccount(username=cfg['mail']['id'],password=f.decrypt(passw).decode("utf-8"))

    config = Configuration(server="outlook.office365.com", credentials=credentials)
    account = Account(primary_smtp_address=cfg['mail']['id'], config=config,autodiscover=False, access_type=DELEGATE)

    send_email(account,subject, body, [cfg['internal']['id']],attachments=[])
