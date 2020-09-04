from django.urls import path
from . import views

app_name = 'words'

urlpatterns = [
    path('', views.todays_word, name='todays_word'),
    path('history', views.word_history, name='history'),
]