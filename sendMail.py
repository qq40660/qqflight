# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import *


from_to = 'beijing-shanghai'
date = 'datetime'
flightNo = 'flightNo'


def send_error_mail(mail_to, from_to, date, flightNo):
    smtp = smtplib.SMTP()
    smtp.connect(MAIL_HOST, MAIL_PORT)
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
    html = html_1 % (from_to, date, flightNo)
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = MAIL_USERNAME
    msg['To'] = 'mail_to'
    msg['Subject'] = title
    for i in mail_to:
        print i
        smtp.sendmail(MAIL_USERNAME, i, msg.as_string())
    smtp.quit()

#send_error_mail(MAIL_TO, from_to, date, flightNo)