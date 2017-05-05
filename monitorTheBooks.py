#!coding=utf-8
#监控图书馆书籍状态并发送邮件提醒
#适用于心仪的图书被借光了的情况，当有人还书，该书的状态变为可借时自动发送邮件提醒
#（使用139邮箱还会有短信提醒，tips:发件人和收件人可以相同）
import requests
import sys
import time
import smtplib
import email.mime.multipart
import email.mime.text
# reload(sys)
# sys.setdefaultencoding('utf8')


bookmysql="http://211.87.177.4/opac/item.php?marc_no=0000377401"
booklinux="http://211.87.177.4/opac/item.php?marc_no=0000387713"
booktest="http://211.87.177.4/opac/item.php?marc_no=0000312783"


while(1):
	time.sleep(600)#秒为单位
	#print("asdg")
	r=requests.get(url=bookmysql)
	r2=requests.get(url=booklinux)
	#r=requests.get(url=booktest)
	text=r.content.decode(encoding="utf-8", errors="strict")
	text2=r2.content.decode(encoding="utf-8", errors="strict")
	if ("可借" in text or "可借" in text2):
		print("发现书籍！")
		####发送邮件
		msg=email.mime.multipart.MIMEMultipart()
		msg['from']='xxxxxxxx@139.com'
		msg['to']='xxxxxxxx@139.com'
		msg['subject']='有书啦！'#主题
		content='''
		    有人还书啦！快去借吧！
		    详情请登录library.upc.edu.cn
		'''
		txt=email.mime.text.MIMEText(content)
		msg.attach(txt)
		smtp=smtplib
		smtp=smtplib.SMTP()
		smtp.connect('smtp.139.com','25')
		smtp.login('xxxxxxxxx@139.com','yourpassword')
		smtp.sendmail('xxxxxxxxxxx@139.com','xxxxxxxxxxx@139.com',str(msg))
		smtp.quit()
		print("邮件发送成功！")
		break
	else:
		print("未发现书籍！")
print("监控结束!")
# print(r.content.decode(encoding="utf-8", errors="strict"))
