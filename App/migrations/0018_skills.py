# Generated by Django 3.2.11 on 2022-01-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_auto_20220113_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill1', models.CharField(max_length=200)),
                ('Skill2', models.CharField(max_length=200)),
                ('Skill3', models.CharField(max_length=200)),
                ('Skill4', models.CharField(max_length=200)),
                ('Skill5', models.CharField(max_length=200)),
            ],
        ),
    ]