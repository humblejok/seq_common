'''
Created on Jul 5, 2013

@author: sdejonckheere
'''
from email.mime.text import MIMEText
import smtplib

SMTP_HOST = '192.168.9.16' # TODO Parameter
SMTP_PORT = 25
SMTP_SENDER = 'sequoia-log@sequoia-ge.com'
SMTP_ADDRESSEES_SEPARATOR = ', '


def send_text_email(addressees, subject, text):
    message = MIMEText(text)
    message['Subject'] = subject
    message['From'] = SMTP_SENDER
    message['To'] = SMTP_ADDRESSEES_SEPARATOR.join(addressees)
    sender = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    sender.sendmail(SMTP_SENDER, addressees, message.as_string())