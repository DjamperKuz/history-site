# Generated by Django 4.2.1 on 2023-05-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historyApp', '0003_remove_question_topic_delete_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]