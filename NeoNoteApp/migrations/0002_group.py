# Generated by Django 3.1.4 on 2021-06-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeoNoteApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
            ],
        ),
    ]
