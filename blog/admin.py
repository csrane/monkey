#blog/admin.py
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' ,'content_size', 'created_at' , 'updated_at' , 'author']


    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = "내용글자수"