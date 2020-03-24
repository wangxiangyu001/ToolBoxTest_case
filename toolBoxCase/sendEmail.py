# coding:utf-8 #设置编码格式

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

mtpserver = 'smtp.qq.com'
def sendEmail():
    sender = '2398679713@qq.com'
    receiver = 'wangxiangyu@sunmi.com'
    username = '2398679713'
    password = 'eikfvcwxkuikecca'


    #
    #
    # # 邮件主题
    mail_title = 'ToolBox自动化测试报告'
    # #
    # #
    # 读取html文件内容
    f = open(r'./report.html', 'rb')
    mail_body = f.read()
    f.close()
    #
    # 创建一个带附件的实例
    message = MIMEText(mail_body, 'html', 'utf-8')
    # message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    # message.attach(MIMEText(mail_body, 'plain', 'utf-8'))

    # 构造附件，传送当前目录下的 html文件
    # att = MIMEText(open(r'./report.html', 'rb').read(), 'base64', 'utf-8')
    # att["Content-Type"] = 'application/octet-stream'
    # att["Content-Disposition"] = 'attachment; filename="ToolBox自动化测试报告.html"'
    # message.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string() )
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

