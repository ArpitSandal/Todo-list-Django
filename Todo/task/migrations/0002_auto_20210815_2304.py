# Generated by Django 2.1.5 on 2021-08-15 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Description',
            new_name='description',
        ),
    ]
