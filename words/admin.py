from django.contrib import admin
from .models import Word

# Register your models here.
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('bgword', 'date' , 'transcript', 'definition', 'partOfSpeech')
    ordering = ['-date']
    search_fields = ('bgword', 'transcript')
    date_hierarchy = 'date'