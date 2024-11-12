from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author', 'title_tag', 'body']  # Exclure 'author' du formulaire
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','id':'admin','type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
