import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = 'mail@mail.com'
receiver_email = 'mail@mail.com'
password = 'password'

# Create message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'example title'

body = """\
body message

"""
message.attach(MIMEText(body, 'plain'))

# Attach file with grepd content
filename = 'ja.csv'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {filename}')

message.attach(part)

# Connect to SMTP server
try:
    server = smtplib.SMTP('smtp.mail.com', 587)  # Use your SMTP server and port
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')

# Close connection
server.quit()
