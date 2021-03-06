# Generated by Django 3.2.11 on 2022-01-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link1', models.URLField(blank=True, max_length=128, verbose_name='Linkedin')),
                ('link2', models.URLField(blank=True, max_length=128, verbose_name='Facebook')),
                ('link3', models.URLField(blank=True, max_length=128, verbose_name='Github')),
                ('link4', models.URLField(blank=True, max_length=128, verbose_name='Google')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image1',
            field=models.ImageField(upload_to='about/', verbose_name='Size 1920*1080 '),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Person Name'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill1',
            field=models.CharField(max_length=200, verbose_name='Skill 95% '),
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill2',
            field=models.CharField(max_length=200, verbose_name='Skill 85% '),
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill3',
            field=models.CharField(max_length=200, verbose_name='Skill 65% '),
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill4',
            field=models.CharField(max_length=200, verbose_name='Skill 85% '),
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill5',
            field=models.CharField(max_length=200, verbose_name='Skill 65% '),
        ),
        migrations.AlterField(
            model_name='work',
            name='image1',
            field=models.ImageField(upload_to='about/', verbose_name='Project Image '),
        ),
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True, max_length=128, verbose_name='Project Link '),
        ),
        migrations.AlterField(
            model_name='work',
            name='projectname',
            field=models.CharField(max_length=200, verbose_name='Project Name '),
        ),
    ]
