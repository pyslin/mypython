
import poplib
import Parser
email = input('Email address:')
password = input('Password:')
pop3_server = input('POP3server:')

#实例化pop3对象
server = poplib.POP3(pop3_server)
server.set_debugleverl(1)
print(server.getwelcome().decode('utf-8'))

#login
server.user(email)
server.pass_(password)

print('邮件数:$s;总大小:$s'%server.stat())
# resp保存服务器的响应码
# mails列表保存每封邮件的编号、大小
resp, mails, octets = server.list()
print(mails)

#传入总长度，也就是获取最后一封邮件
index = len(mails)
#lines是相应邮件所有行数据
resp, lines, octets = server.retr(index)

## 将lines的所有数据（原本是一个字节列表）拼接在一起
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parsestr().parsestr(msg_content)

server.quit()







