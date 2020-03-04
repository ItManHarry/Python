import poplib
import email.parser
import email.policy 
#创建与邮件服务器的连接
#connect = poplib.POP3('pop.qq.com', 10)             #普通连接
connect = poplib.POP3_SSL('pop.qq.com', 995)    #基于SSL的安全连接
connect.set_debuglevel(1)
content = connect.getwelcome().decode('utf-8')
print(content)
#邮箱账户
account = '280688074@qq.com'
#安全码
code = 'fzbifrurnhhwcajd'
#登录服务器
connect.user(account)
connect.pass_(code)
#统计邮件信息
num, size = connect.stat()
print('Email amount : ', num, ' email size : ', size)
#获取邮件列表
respstate, list, other = connect.list()
print('Response state : ', respstate)
print('Mail list : ', list)
#获取指定的邮件 (最后一封)
respstate, data, other = connect.retr(len(list))
print('Response state : ', respstate)
#print('Mail content : ', data)
mailcontent =  b'\r\n'.join(data)
message = email.parser.BytesParser(policy=email.policy .default).parsebytes(mailcontent)
print(type(message))
print('From : ', message['from'])
print('To : ', message['to'])
print('Subject : ', message['subject'])
print('First to : ', message['to'].addresses[0].username)
#遍历邮件内容 - 邮件每个部分都是一个part
for part in message.walk():
    print('Content type is : ', part.get_content_type())
    #'multipart'代表是邮件内容的容器，无需处理
    if part.get_content_type() == 'multipart':
        continue
     #'text'代表是邮件内容，执行打印
    elif part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
        print(part.get_content())
        #continue
    #剩下的就是附件
    else:
        file= part.get_filename()
        print('fiel type is : ',type(file))
        #with open(file, 'wb') as f:
            #f.write(part.get_payload(decode=True))
#断开服务器
connect.quit()            