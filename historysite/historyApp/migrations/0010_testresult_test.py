# Generated by Django 4.2.1 on 2023-05-31 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historyApp', '0009_testresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='historyApp.topic'),
        ),
    ]
