from celery import shared_task
from django.core.mail import send_mail
from sendjoke import settings
import requests
from .models import Email
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task(bind=True)
def send_mail_func(self):
    emails = Email.objects.all()
    headers = { "User-Agent": "sendjokes kespeakup772@gmail.com", "Accept": "text/plain"} 
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers = headers)
    txt = response.text
    for email in emails:
        mail_subject = " Joke of the day"
        message = txt
        to_email = email.email
        html_message = render_to_string('joke/email.html', {'message': message})
        plain_message = strip_tags(html_message)
        send_mail(
            subject=mail_subject,
            message= plain_message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list= [to_email], 
            html_message= html_message,
            fail_silently= False
        )
    

#uuxnhbfrlvjafqba