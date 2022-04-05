from django.db import models

# Create your models here.
'''Database in here'''
'''CODE: Don't need to comment bellow a function or a class'''

class Tag(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=False)
    price = models.FloatField(null=False)
    image = models.TextField()
    author = models.CharField(max_length=200)
    descript = models.TextField(null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
