# Generated by Django 3.2.11 on 2022-01-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_alter_work_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
