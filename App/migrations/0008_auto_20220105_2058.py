# Generated by Django 3.2.11 on 2022-01-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_remove_portfolio_description2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='description1',
            new_name='description',
        ),
    ]
