from django import forms
from .models import bloglar


class blogform(forms.ModelForm):
    class Meta:
        model = bloglar
        fields = ['title','text']