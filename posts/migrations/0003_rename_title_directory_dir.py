# Generated by Django 4.2.2 on 2023-06-19 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_directory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directory',
            old_name='title',
            new_name='dir',
        ),
    ]
