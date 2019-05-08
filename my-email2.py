#!/usr/bin/python3
#-*-coding:UTF-8-*-
#SMTP电子邮件发送
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr,formataddr
#先定义署名格式化函数
def _format_addr(s):
    #从u'python爱好者<addr>'中分离为两个元素(是Unicode编码)组成的tuple:(u'python爱好者',u'addr')
    #再格式化
    name, addr = parseaddr(s)
    #formataddr 要传入tuple （）
    return formataddr((Header(name, 'utf-8').encode(), addr))

#发送人，接收人
sender = 'py78xxx@163.com'
pwd = 'hb0714' #请自行登陆邮箱打开SMTP服务，会自动生成第三方授权码，不是登陆密码！
receiver = 'xingkemo2017@icloud.com'


#MIMEMultipart实例化，格式化的署名和接收人信息
message=MIMEMultipart()
message['From'] = _format_addr('这是xx<%s>'%sender)
message['To'] = _format_addr('发给<%s>'%receiver)
message['Subject'] = Header('我是标题！！','utf').encode()
#正文是attach（MIMEText）
message.attach(MIMEText('<html><body>'
                        +'<h1>Hello</h1>'
                        +'<p>礼物<img src="cid:Imgid">'
                        +'</body></html>','html','utf-8'))

#MIMEImage，只要打开相应图片，再用read()方法读入数据，指明src中的代号是多少，如这里是'Imgid’，在HTML格式里就对应输入。
with open('d:/mypython/test.jpg','rb') as f:
    #打开，读取，传入
    mime=MIMEImage(f.read())
    mime.add_header('Content-ID','Imgid')
    #附件也是attach（MIMEImage）
    message.attach(mime)

#发送邮件！
try:
    #实例化，先创建SSL安全连接，然后再使用SMTP协议发送邮件
    smtpobj=smtplib.SMTP_SSL('smtp.163.com',465)
    smtpobj.login(sender,pwd)
    smtpobj.sendmail(sender,[receiver],message.as_string())
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，Case:%s'%e)
