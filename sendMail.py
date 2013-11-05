# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import *

from_to = 'beijing-shanghai'
date = 'datetime'
flightNo = 'flightNo'

html_1 = '''
<!DOCTYPE html>
<html>
<head>
    <title>Error Warring</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<div id="title">
    <h2>QQ Flight Auto_test Error or Warring Report</h2>
</div>
<div>
    <p>无结果</p>
    <p>城市：</p>
    <p>航班日期：</p>
    <p>航班号：</p>
</div>
</body>
</html>
'''

def send_regist_mail(mail_to):
    try:
        title = 'QQ Flight Test Result'
        __send_mail(mail_to, title)
        return True
    except:
        return False


def __send_mail(title):
    smtp = smtplib.SMTP()
    smtp.connect(MAIL_HOST, MAIL_PORT)
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD)

    msg = MIMEText(html_1, 'html', 'utf-8')
    msg['From'] = MAIL_USERNAME
    msg['To'] = '35318718'
    msg['Subject'] = title
    smtp.sendmail(MAIL_USERNAME, '35318717@qq.com', msg.as_string())
    smtp.quit()

