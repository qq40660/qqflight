 # -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import *

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
    <p>关键字 “酷讯担保”没有出现在结果中</p>
    <p>城市： %s</p>
    <p>航班日期： %s</p>
    <p>航班号： %s</p>
</div>
</body>
</html>
'''

smtp = smtplib.SMTP()
smtp.connect(MAIL_HOST, MAIL_PORT)
smtp.login(MAIL_USERNAME, MAIL_PASSWORD)

msg = MIMEText(html_1, 'html', 'utf-8')
msg['From'] = MAIL_USERNAME
msg['To'] = '35318718'
msg['Subject'] = title
smtp.sendmail(MAIL_USERNAME, '35318717@qq.com', msg.as_string())
smtp.quit()