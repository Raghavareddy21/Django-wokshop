from django.shortcuts import render
from .models import Post, Category
from . import forms
from django.http import HttpResponse


def home(request):
	return HttpResponse("Hello World")

def posts(request):
	posts = Post.objects.order_by('-date')
	categories = Category.objects.all()	
	return render(request, 'blog/posts.html',{'posts': posts, 'categories': categories})

def categorylist(request):
	categories = Category.objects.all()
	return render(request, 'blog/categories.html',{'category_list':categories})

def blogPost(request):
	if request.method == 'POST':
		form = forms.addPost(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("The post has been saved")
		else:
			return HttpResponse("The form is not valid")
	else:
		form = forms.addPost(request.POST)
		return render(request, 'blog/addPost.html', {'form':form})