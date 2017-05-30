from django import forms
from .models import Post, Topico

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PaginaForm(forms.ModelForm):

    class Meta:
        model = Topico
        fields = ('title',)
