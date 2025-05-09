from django.urls import path
from .views import ListSSLView
from .views import ssl_view

urlpatterns = [
    path('ssl_view/', ListSSLView.as_view()),
    path('ssl/', ssl_view, name='ssh_view'),
]
