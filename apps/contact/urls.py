from django.urls import path
from apps.contact.views import ContactListAPIView

urlpatterns = [
    path('contacts/', ContactListAPIView.as_view(), name='contact-list'),
]
