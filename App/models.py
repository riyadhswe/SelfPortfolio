from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name