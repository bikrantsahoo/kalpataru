import smtplib
# from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.constants import constants


def send_email(recipient_email, subject, message_template):
    try:
        server = smtplib.SMTP(constants.SMTP_SERVER, constants.SMTP_PORT)
        server.starttls()
        server.login(constants.SENDER_MAIL, constants.SENDER_PASSWORD)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = constants.SENDER_MAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        # msg.attach(MIMEText(message_template, 'plain'))

        # Send the email
        server.sendmail(constants.SENDER_MAIL, recipient_email, message_template)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send the notification: {str(e)}")
        return False
