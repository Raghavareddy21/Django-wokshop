from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^Home/$',views.home,name="home"),
	url(r'^categories/$',views.categorylist,name="categorylist"),
	url(r'^posts/$', views.posts, name="postslist")
	]