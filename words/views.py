from django.shortcuts import render
from django.core.mail import send_mail
from django import forms
from .models import Word
import datetime

# Create your views here.
def todays_word(request):

    today = datetime.date.today()
    word = Word.objects.get(date=today)
    subject = 'Your daily Bulgarian word!'
    message = f'The word for {today} is {word.bgword}, ({word.partOfSpeech}). \nIt is pronounced /{word.transcript}/ and its meaning is {word.definition}.'

    if request.method == 'POST':
        send_mail(subject, message, 'baldrianmockingjay@gmail.com', [request.POST.get('email')])

    return render(request,
                    'words/pages/index.html',
                    {'word': word})

def word_history(request):
    words = Word.objects.all().order_by('-date')
    return render(request,
                    'words/pages/history.html',
                    {'words': words})