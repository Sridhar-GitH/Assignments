import smtplib
from email.message import EmailMessage
import ssl
import os


sender = 'sridharupskills@gmail.com'
password = os.environ.get('DB_PASSWORD')
receiver = 'sridharupskills@gmail.com'

subject = 'sent from python'
body = 'this is python code '


msg = EmailMessage()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.set_content(body)

context = ssl.create_default_context()
print('processing...')
with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as server:
    server.login(sender,password)

    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
print('done it !')
