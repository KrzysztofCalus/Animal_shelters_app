# Generated by Django 3.2.4 on 2021-07-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0007_alter_animaltype_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltype',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]