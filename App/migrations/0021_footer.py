# Generated by Django 3.2.11 on 2022-01-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_auto_20220113_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer', models.CharField(max_length=200, verbose_name='Footer')),
            ],
        ),
    ]
