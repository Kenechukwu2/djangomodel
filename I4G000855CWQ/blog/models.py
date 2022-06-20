from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add= True)
    publish_on = models.DateTimeField(auto_now= True)