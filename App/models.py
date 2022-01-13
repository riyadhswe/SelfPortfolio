from django.db import models


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
    name = models.CharField(max_length=200, null=True,verbose_name='Tittle')
    image1 = models.ImageField(upload_to='about/', blank=False,verbose_name='Size 1920*1080 ')
    image2 = models.ImageField(upload_to='about/', blank=False)
    image3 = models.ImageField(upload_to='about/', blank=False)




class Pdf(models.Model):
    name = models.CharField(max_length=200, null=True)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.id

class Work(models.Model):
    projectname = models.CharField(max_length=200)
    link = models.URLField(max_length=128,blank=True)
    image1 = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.projectname

class Skills(models.Model):
    Skill1 = models.CharField(max_length=200)
    Skill2 = models.CharField(max_length=200)
    Skill3 = models.CharField(max_length=200)
    Skill4 = models.CharField(max_length=200)
    Skill5 = models.CharField(max_length=200)

