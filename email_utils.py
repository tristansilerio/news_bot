import smtplib
import ssl
import config
import email.mime.text
import email.mime.multipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formatdate

def send_email(subject, body, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = config.TO_EMAIL_ADDRESS
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    print(msg)

    if attachments:
        for filename, filepath in attachments.items():
            with open(filepath, "rb") as f:
                attachment = MIMEApplication(f.read(), _subtype=filename.split("/")[-1])
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(attachment)

    # Create an SSL context
    context = ssl.create_default_context()

    # Use SMTP (non-SSL) or SMTP_SSL (SSL/TLS) based on your server configuration
    with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT, context=context) as server:
        server.login(config.EMAIL_ADDRESS, config.APP_PASSWORD)
        server.sendmail(config.EMAIL_ADDRESS, config.TO_EMAIL_ADDRESS, msg.as_string())

# Example usage
#send_email("Test Subject", "This is the email body.")
