from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.AutoField(primary_key=True)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()



# Create your models here.
