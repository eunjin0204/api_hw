from django.db import models
from django.conf import settings

# Create your models here.

class UserPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

# 1번 : eunjin
# 2번 : sujin

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to="files")
    desc = models.CharField(max_length=100)