# Generated by Django 3.2.11 on 2022-01-05 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_name_name_allname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='allname',
            new_name='name',
        ),
    ]
