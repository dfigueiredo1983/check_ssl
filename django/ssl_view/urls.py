from django.urls import path
from .views import ListSSLView

urlpatterns = [
    path('', ListSSLView.as_view(), name='home'),
    path('ssl_view/', ListSSLView.as_view(), name='ssl_view'),
]
