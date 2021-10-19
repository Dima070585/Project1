from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    technology = models.CharField(max_length=40)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    content = RichTextUploadingField()
    image = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prise = models.IntegerField()

    def __str__(self):
        return self.title

