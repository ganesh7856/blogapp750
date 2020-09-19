from django import forms
from .models import *
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = ['title','content','date_posted','image','author']


class CommentsForm(forms.ModelForm):
    content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control',
                                                         'placeholder':'Text goes here...!!!' ,
                                                         'rows':4,'cols':'50'}))
    class Meta:
        model=Comments
        fields=['content']