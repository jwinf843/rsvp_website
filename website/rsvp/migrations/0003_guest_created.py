# Generated by Django 2.0.4 on 2018-05-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_guest_rsvp'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]