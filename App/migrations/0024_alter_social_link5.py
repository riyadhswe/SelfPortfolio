# Generated by Django 3.2.11 on 2022-01-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_alter_social_link5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='link5',
            field=models.URLField(blank=True, max_length=20, verbose_name='Phone'),
        ),
    ]
