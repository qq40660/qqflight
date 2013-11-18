#coding: utf-8

#urlHead
bhHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate='
bgHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=CAN&depDate='
hgHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=SHA&toCity=CAN&depDate='


#email setting
MAIL_HOST = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USERNAME = '35318717@qq.com'
MAIL_PASSWORD = '3218818ice'
MAIL_TO = ['35318717@qq.com', '304858826@qq.com']

title = 'QQ Flight Auto_test Error or Warring Report'


html_1 = """
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
    <p>城市：%s</p>
    <p>航班日期：%s</p>
    <p>航班号：%s</p>
</div>
</body>
</html>
"""
