# Generated by Django 3.2.4 on 2021-07-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0009_auto_20210715_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
