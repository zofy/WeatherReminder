# # Import smtplib for the actual sending function
# import smtplib
#
# # Import the email modules we'll need
# from email.mime.text import MIMEText
#
# # Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# # fp = open(textfile, 'rb')
# # Create a text/plain message
# # msg = MIMEText(fp.read())
# msg = MIMEText('Hello can you hear me?')
# # fp.close()
#
# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'The contents of mail'
# msg['From'] = 'me'
# msg['To'] = 'zofy11@gmail.com'
#
# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail('me', 'zofy11@gmail.com', msg.as_string())
# s.quit()


# import smtplib
#
# sender = 'zofy11@gmail.com'
# receivers = ['zofy11@gmail.com']
#
# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test
#
# This is a test e-mail message.
# """
#
# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)
#    print "Successfully sent email"
# except smtplib.SMTPException:
#    print "Error: unable to send email"


import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'zofy11@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'zofy11@gmail.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('zofy11@gmail.com', ['zofy11@gmail.com'], msg.as_string())
finally:
    server.quit()
