#MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol
#MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3
# IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，
# 还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。


#第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = Header('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')



#实例化，smtp端口25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
#登录
server.login(from_addr, password)
#收件地址list，可以多个，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()