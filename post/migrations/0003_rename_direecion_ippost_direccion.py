# Generated by Django 4.1.5 on 2023-01-16 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_iplist_ippost_direecion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ippost',
            old_name='direecion',
            new_name='direccion',
        ),
    ]
