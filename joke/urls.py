from django.urls import path
from .views import AcceptEmail

urlpatterns = [
    path('', AcceptEmail.as_view(), name='joke-home' ),
]