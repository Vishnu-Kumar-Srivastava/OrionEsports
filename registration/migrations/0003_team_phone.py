# Generated by Django 4.1.5 on 2023-01-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_participant_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
