from django.contrib import admin
from .models import Post,Comment,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','created','title','body','owner']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','created','body','owner','post']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','owner']
