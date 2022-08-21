from curses.ascii import CR
from django.shortcuts import render
from django.views.generic import CreateView
from . models import Email
from .tasks import send_mail_func

class AcceptEmail(CreateView):
    model = Email
    fields = ['email',]
    success_url = '/'
    #send_mail_func.delay()


# Create your views here.
