import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import smtplib


if __name__ == '__main__':
    loder = unittest.TestLoader()
    suite = loder.loadTestsFromName("TestClass")
    print(suite)
    filename = time.strftime("%Y-%m-%d-%H_%M_%S") + "res.html"
    with open(filename, "wb") as f:
        runner = HTMLTestRunner(f, verbosity=2, title="单元测试报告", description="第一次运行结果")
        runner.run(suite)

    #获取报告内容
    htmlreport = None
    with open(filename, 'rb') as f:
        htmlreport = f.read()

    #构建邮件
    mail = MIMEText(htmlreport, 'html', 'utf-8')
    mail['Subject'] = Header(f'邮件自动化{filename}', 'utf-8')
    mail['From'] = formataddr(['JInpeng_Wang', '1832508189@qq.com'])
    mail['to'] = '18770766249@163.com'

    #添加附件
    mp = MIMEMultipart()
    mail2 = MIMEText(htmlreport, 'base64', 'utf-8')
    mail2['Content-Type'] = "application/octet-stream"
    print(filename)
    mail2['Content-Disposition'] = f'attachment;filename={filename}'
    mp['Subject'] = Header(f'邮件自动化附件', 'utf-8')
    mp['From'] = formataddr(['JInpeng_Wang', '1832508189@qq.com'])
    mp['to'] = '18770766249@163.com'
    mp.attach(mail2)

    ##构建SMTP对象
    smpt = smtplib.SMTP()
    smpt.connect("smtp.qq.com")
    smpt.login('1832508189@qq.com', 'wlcydcooamluceah')
    smpt.sendmail('1832508189@qq.com', '18770766249@163.com', mail.as_string())
    smpt.sendmail('1832508189@qq.com', '18770766249@163.com', mp.as_string())
    smpt.quit()