# Generated by Django 4.2.1 on 2023-05-28 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyApp', '0006_remove_topic_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
