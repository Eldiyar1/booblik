from django.urls import path
from .views import FilialListAPIView, FilialRetrieveAPIView, ContactListAPIView, MusicListAPIView, ImageListAPIView, \
    AboutMeListAPIView, AboutMeFactListAPIView

urlpatterns = [
    path("filials/", FilialListAPIView.as_view(), name="location-list-create"),
    path("filials/<int:pk>/", FilialRetrieveAPIView.as_view(), name="location-detail", ),
    path('contacts/', ContactListAPIView.as_view(), name='contact-list'),
    path('music/', MusicListAPIView.as_view(), name='music-list'),
    path('images/', ImageListAPIView.as_view(), name='image-list'),
    path('about-me/', AboutMeListAPIView.as_view(), name='about-me-list'),
    path('about_me_facts/', AboutMeFactListAPIView.as_view(), name='about_me_fact_list'),

]
