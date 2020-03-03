import smtplib
import email.message as em
import email.utils as eu
#邮箱账户
account = '280688074@qq.com'
#安全码
code = 'fzbifrurnhhwcajd'
#连接SMTP服务器
# smtplib.SMTP()          #普通的SMTP连接
#server = smtplib.SMTP_SSL('smtp.qq.com',, 21)
# smtplib.SMTP_SSL()  #基于SSL的SMTP连接
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.set_debuglevel(1)
#登录邮箱服务器
server.login(account, code)
#创建邮件对象
message = em.EmailMessage()
#设置邮件内容 - 普通邮件
#message.set_content('The mail from python application.')
#设置邮件内容 - HTML邮件
att_id1 = eu.make_msgid()
message.set_content("""
    <h2>The mail from python application.</h2>
    <div style = 'border:1px solid red'>HTML邮件内容</div>
    <img src = 'cid:%s' width = '200' height = '120'/>
""" %att_id1[1:-1], 'html', 'utf-8')
#设置邮件标题
message['subject']='HTML邮件测试-带有附件'
#设置发件人
message['from']='Harry <%s>' %account
#设置收件人
message['to']='ChengGuoqian <%s>' %'guoqian.cheng@doosan.com'
#添加附件 - 二进制读取
#如果正文要引用附件则添加cid属性，否则不需要
with open('e:/th.jpg', 'rb') as f:
    message.add_attachment(f.read(), maintype='image',subtype='jpeg',filename='picture.jpg',cid=att_id1)
with open('e:/harry.jpg', 'rb') as f:
    message.add_attachment(f.read(), maintype='image',subtype='jpeg',filename='me.jpg')    
with open('e:/test.xlsx', 'rb') as f:
    message.add_attachment(f.read(), maintype='file',subtype='excel',filename='test.xlsx')      
#执行邮件发送
server.sendmail(account, ['guoqian.cheng@doosan.com'], message.as_string())
#断开连接
server.quit()