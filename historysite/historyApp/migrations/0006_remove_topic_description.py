# Generated by Django 4.2.1 on 2023-05-28 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyApp', '0005_topic_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
    ]
