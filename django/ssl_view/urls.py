from django.urls import path
from .views import ListSSLView

urlpatterns = [
    path('', ListSSLView.as_view(), name='home'),
]
