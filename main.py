'''
Authors: Monsef ALAHEM
sumerize: the progam send a message to all emails file with attachements
'''


#auto email tools
from email.mime.text import MIMEText
#from email.header import Header
from smtplib import SMTP_SSL

# from os.path import basename
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate
# from email.mime.base import MIMEBase
# import os

# Import smtplib for the actual sending function
import smtplib

# And imghdr to find the types of our images
import imghdr

# Here are the email package modules we'll need
from email.message import EmailMessage

import time


# email sending server
host_server = 'smtp.gmail.com' #exmeple 'smtp.exmail.qq.com'
sender_mail = 'your_email@gmail.com'
sender_passcode = 'your_password'


def send_mail(receiver='', mail_title='', mail_content='',files=None):
    # ssl login
    smtp = SMTP_SSL(host_server, 465) #465 587
    print("ssl session success !")
    # set_debuglevel() for debug, 1 enable debug, 0 for disable
    # smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    print("ehlo success !")
    smtp.login(sender_mail, sender_passcode)
    print("login success !")

    # construct message
    msg = EmailMessage()
    msg.set_content(mail_content)
    msg["Subject"] = mail_title
    msg["From"] = sender_mail
    msg["To"] = receiver

    for file in files:
        with open(file, 'rb') as fp:
            data = fp.read()
        msg.add_attachment(data,maintype='Excel', subtype='document',filename=file)

    smtp.sendmail(sender_mail, receiver, msg.as_string())
    smtp.quit()

#loading a file an sending mail for e-mail in file
f = open("contact.txt","r")

for line in f:
    receiver = str(line)
    mail_content = "your_message"
    mail_title = "your_title"
    receiver = receiver[:-1]
    print(receiver)
    send_mail(receiver=receiver,mail_title=mail_title,mail_content="hello ! im'auto-mailler", files={'your_file1','your_file2'})
    time.sleep(1)

f.close()