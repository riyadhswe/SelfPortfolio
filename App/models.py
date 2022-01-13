from django.db import models
from django.apps import apps


# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name='Person Name')
    image1 = models.ImageField(upload_to='about/', blank=False,verbose_name='Profile 400*458 ')
    image2 = models.ImageField(upload_to='about/', blank=False,verbose_name='About 640*841 ')
    image3 = models.ImageField(upload_to='about/', blank=False,verbose_name='Skill 640*426 ')




class Pdf(models.Model):
    name = models.CharField(max_length=200, null=True)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.name

class Work(models.Model):
    projectname = models.CharField(max_length=200,verbose_name='Project Name ')
    link = models.URLField(max_length=128,blank=True,verbose_name='Project Link ')
    image1 = models.ImageField(upload_to='about/', blank=False,verbose_name='Work 640*426 ')

    def __str__(self):
        return self.projectname

class Skills(models.Model):
    Skill1 = models.CharField(max_length=200,verbose_name='Skill 95% ')
    Skill2 = models.CharField(max_length=200,verbose_name='Skill 85% ')
    Skill3 = models.CharField(max_length=200,verbose_name='Skill 65% ')
    Skill4 = models.CharField(max_length=200,verbose_name='Skill 85% ')
    Skill5 = models.CharField(max_length=200,verbose_name='Skill 65% ')

class Social(models.Model):
    link1 = models.URLField(max_length=128,blank=True,verbose_name='Linkedin')
    link2 = models.URLField(max_length=128,blank=True,verbose_name='Facebook')
    link3 = models.URLField(max_length=128,blank=True,verbose_name='Github')
    link4 = models.EmailField(max_length=128,blank=True,verbose_name='Google')

class footer(models.Model):
    footer = models.CharField(max_length=200,verbose_name='Footer')

    def __str__(self):
        return self.footer

