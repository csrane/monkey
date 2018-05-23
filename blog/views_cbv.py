from django import forms
from django.views.generic import ListView, CreateView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)

#blog.forms.py 가 있다 가정
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' 


class PostCreatView(CreateView):
    model = Post
    form_class = PostForm


post_new = PostCreatView.as_view()