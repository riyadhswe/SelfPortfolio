# Generated by Django 3.2.11 on 2022-01-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20220105_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description1',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description2',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
