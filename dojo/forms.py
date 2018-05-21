#dojo/forms.py
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하세요.')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    contents = forms.CharField(widget=forms.Textarea)
