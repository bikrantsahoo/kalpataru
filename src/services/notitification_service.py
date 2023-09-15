from flask_mail import Message
from flask import current_app, render_template
from . import mail  # Import the mail instance from your app


def send_email(subject, recipients, template, **kwargs):
    msg = Message(subject=subject,
                  recipients=recipients,
                  sender=current_app.config['MAIL_DEFAULT_SENDER'])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
