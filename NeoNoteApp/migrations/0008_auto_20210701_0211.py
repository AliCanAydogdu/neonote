# Generated by Django 3.1.4 on 2021-07-01 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NeoNoteApp', '0007_auto_20210701_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeoNoteApp.group'),
        ),
        migrations.AlterField(
            model_name='places',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
