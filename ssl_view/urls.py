from django.urls import path
from .views import Certificate_SSL_View

urlpatterns = [
    path('ssl/', Certificate_SSL_View.as_view()),
]
