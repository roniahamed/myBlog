from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __self__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'authored_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, related_name = 'categorized_posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self):
        return f'comment by {self.author.username} on {self.post.title}'

