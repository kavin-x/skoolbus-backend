from django.urls import path
from Oauth.views import index

urlpatterns = [
    path('', index),
]