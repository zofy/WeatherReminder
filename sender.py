import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = 'zofy11@gmail.com'
to_address = 'zofy11@gmail.com'
text = 'test message sent from Python'
username = 'xxxxx'
password = 'xxxxx'
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


class MailManager(object):
    my_address = 'yourweatherapp@gmail.com'
    username = 'yourweatherapp'
    password = 'xxxxxxxxx'

    def __init__(self, to_address, text=''):
        self.to_address = to_address
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.text = text
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = 'Weather forecast'
        msg.attach(MIMEText(text))

    def login_to_server(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(username, password)

    def send_forecast(self):
        self.server.sendmail(from_address, to_address, msg.as_string())
        self.server.quit()
