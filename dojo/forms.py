#dojo/forms.py
from django import forms
from .models import GameUser, Post




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title','content','user_agent']
        widgets = {
            'user_agent' : forms.HiddenInput,
        }


    '''
    def save(self, commit=True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return post 
    '''

class GameUserSigupForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = '__all__'

    def clean_username(self):
        return self.cleaned_data.get('username', '').strip()

