# Generated by Django 3.2.11 on 2022-01-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20220105_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description1',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description2',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]