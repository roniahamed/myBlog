from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_at', 'is_published')
    list_filter = ('is_published', 'category', 'tags')
    search_fields = ('title', 'content')
    autocomplete_fields = ('category', 'tags')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username', 'post__title')
    autocomplete_fields = ('post', 'author')
