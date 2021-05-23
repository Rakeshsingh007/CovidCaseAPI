from django.urls import path
from . import views

app_name = 'webscraper'

urlpatterns = [
    path('covid-case-info/', views.CovidCaseWebScraper.as_view()),
]
