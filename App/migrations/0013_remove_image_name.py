# Generated by Django 3.2.11 on 2022-01-13 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
