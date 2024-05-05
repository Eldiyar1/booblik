from django.urls import path
from .views import FilialListAPIView, FilialRetrieveAPIView, ContactListAPIView

urlpatterns = [
    path("filials/", FilialListAPIView.as_view(), name="location-list-create"),
    path("filials/<int:pk>/", FilialRetrieveAPIView.as_view(), name="location-detail",),
    path('contacts/', ContactListAPIView.as_view(), name='contact-list'),
]
