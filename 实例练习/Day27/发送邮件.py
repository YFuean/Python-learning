'''
发送邮件
'''

import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
# 负责构造邮件头信息
from email.header import Header
# SMIP服务器，这里使用qq邮箱
mail_host = "smtp.qq.com"
# 发件人邮箱
mail_sender = "1412666584@qq.com"
# 邮箱授权码
mail_license = "nayutnzzfatdbagb"
# 收件人邮箱
mail_receivers = ["1412666584@qq.com", "16422802@qq.com",
                  "1321339159@qq.com", "1299088269@qq.com"]
# 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件
mm = MIMEMultipart('related')
# 邮件主题
subject_content = """Python测试邮件"""
# 设置发送者
mm["From"] = "岳凡<1412666584@qq.com>"
# 设置接收者
mm["To"] = "我<1412666584@qq.com>,许老师<16422802@qq.com>,tony<1321339159@qq.com>,田震<1299088269@qq.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content, 'utf-8')
# 邮件正文内容
body_content = """hello,这里是python发出的邮件——岳凡"""
# 构造文本，参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content, "plain", "utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)
# 构造附件
atta = MIMEText(open('./res/excel/excel_demo2.xlsx',
                     'rb').read(), 'base64', 'utf-8')
# 设置附件信息
atta["Content-Disposition"] = 'attachment; filename="excel_demo2.xlsx"'
# 添加附件到邮件信息当中去
mm.attach(atta)
# 创建SMTO对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# stp.set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender, mail_license)
# 发送邮件，参数1：发件人邮箱，参数2：收件人邮箱，参数3：把邮箱内容转成str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("发送成功")
# 关闭
stp.quit()
