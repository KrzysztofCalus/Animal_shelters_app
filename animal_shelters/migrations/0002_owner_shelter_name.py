# Generated by Django 3.2.4 on 2021-07-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='shelter_name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
