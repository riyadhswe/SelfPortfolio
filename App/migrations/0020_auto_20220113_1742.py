# Generated by Django 3.2.11 on 2022-01-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_auto_20220113_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image1',
            field=models.ImageField(upload_to='about/', verbose_name='Profile 400*458 '),
        ),
        migrations.AlterField(
            model_name='image',
            name='image2',
            field=models.ImageField(upload_to='about/', verbose_name='About 640*841 '),
        ),
        migrations.AlterField(
            model_name='image',
            name='image3',
            field=models.ImageField(upload_to='about/', verbose_name='Skill 640*426 '),
        ),
        migrations.AlterField(
            model_name='social',
            name='link4',
            field=models.EmailField(blank=True, max_length=128, verbose_name='Google'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image1',
            field=models.ImageField(upload_to='about/', verbose_name='Work 640*426 '),
        ),
    ]
