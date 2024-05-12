from django.urls import path

from apps.vacancy.views import VacancyListView, VacancyDetailView, SendResumeView, VacancyListBotView

urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/<int:vacancy_id>/send-resume/', SendResumeView.as_view(), name='send-resume'),
    path('vacancies/bot/', VacancyListBotView.as_view(), name='vacancy-list-bot'),
]
