# Generated by Django 5.1 on 2024-09-08 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='waiting_people',
            field=models.CharField(max_length=100),
        ),
    ]
