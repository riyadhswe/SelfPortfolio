# Generated by Django 3.2.11 on 2022-01-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='pdf',
        ),
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True, db_index=True, max_length=128, unique=True),
        ),
    ]