from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class BlogHome(ListView):
	model = Post
	template_name = 'blog.html'

class ArticleListView(ListView):
	model = Post
	template_name = 'blog_list.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'blog_details.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'add_post.html'
	#fields = '__all__'
	fields =('title', 'tital_tag', 'body')