# Generated by Django 3.1.4 on 2021-07-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NeoNoteApp', '0012_auto_20210701_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='folder',
        ),
    ]
