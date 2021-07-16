# Generated by Django 3.2.4 on 2021-07-15 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0012_auto_20210715_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalcare',
            name='animal',
        ),
        migrations.AddField(
            model_name='animalcare',
            name='animal',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='animal_shelters.animal'),
        ),
    ]
