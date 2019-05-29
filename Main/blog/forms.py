from django import forms
from .models import Post, Category, Tag

class addPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','date','content','category','tags','author')