import threading
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def send_email(subject, message, recipient_email):

    def _send():
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[recipient_email],
        )

    thread = threading.Thread(target=_send)
    thread.daemon = True
    thread.start()


