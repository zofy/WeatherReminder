import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = 'zofy11@gmail.com'
to_address = 'zofy11@gmail.com'
text = 'test message sent from Python'
username = 'zofy11'
password = 'kriziceq'
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = 'Weather forecast'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()
