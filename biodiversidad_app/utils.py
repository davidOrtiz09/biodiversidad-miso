#!/usr/bin/env python

from biodiversidad_miso.settings import DEFAULT_FROM_EMAIL
from threading import Thread
from django.core.mail import EmailMessage


class EmailThread(Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, DEFAULT_FROM_EMAIL, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()


def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()
