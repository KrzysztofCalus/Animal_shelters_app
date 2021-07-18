# Generated by Django 3.2.4 on 2021-07-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0008_alter_animaltype_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='picture',
            field=models.ImageField(blank=True,
                                    null=True,
                                    upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='picture',
            field=models.ImageField(blank=True,
                                    null=True,
                                    upload_to='images/'),
        ),
    ]
