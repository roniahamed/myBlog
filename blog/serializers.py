from rest_framework import serializers 
from .models import Category, Tag, Post, Comment 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['id', 'content', 'created_at', 'author', 'post']
    
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','title','content', 'published_at','is_published', 'author', 'category', 'tags', 'comments']

