from django.shortcuts import render
from .models import Post, Category
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

#def blogPost(request):
#	if request.method == 'POST':
#		title