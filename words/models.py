from django.db import models

# Create your models here.

class Word(models.Model):
    NOUN = 'N'
    ADJECTIVE = 'ADJ'
    VERB = 'V'
    ADVERB = 'ADV'
    PARTS_OF_SPEECH_CHOICES = [
        (NOUN, 'Noun'),
        (ADJECTIVE, 'Adjective'),
        (VERB, 'Verb'),
        (ADVERB, 'Adverb')
    ]
    date = models.DateField()
    bgword = models.CharField(max_length=50, unique_for_date='date')
    partOfSpeech = models.CharField(
        max_length=9,
        choices=PARTS_OF_SPEECH_CHOICES,
        default=NOUN
    )
    transcript = models.CharField(max_length=75)
    definition = models.CharField(max_length=50)

    class Meta:
        db_table = 'daily_words'

    def __str__(self):
        return self.transcript