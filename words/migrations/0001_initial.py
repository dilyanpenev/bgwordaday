# Generated by Django 3.0.9 on 2020-08-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bgword', models.CharField(max_length=50, unique_for_date=models.DateField())),
                ('partOfSpeech', models.CharField(choices=[('N', 'Noun'), ('ADJ', 'Adjective'), ('V', 'Verb'), ('ADV', 'Adverb')], default='N', max_length=9)),
                ('transcript', models.CharField(max_length=75)),
                ('definition', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
