from django.shortcuts import render
from .models import Word
import datetime

# Create your views here.
def todays_word(request):
    return render(request,
                    'words/pages/index.html',
                    {'word': Word.objects.get(date=datetime.date.today())})