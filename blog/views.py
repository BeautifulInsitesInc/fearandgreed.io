from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def category_list(request):
#   #categories = Category.objects.all()
#    return render (request, 'blog/category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

class BlogHome(ListView):
	model = Post
	template_name = 'blog.html'
	ordering = ['-created_at']

	def get_context_date(self, *args, **kwargs):
		cat_menu = Category.objects.all
		context = super(BlogHome, self).get_context_date(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class ArticleListView(ListView):
	model = Post
	template_name = 'blog_list.html'
	ordering = ['-created_at']

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})
	
class ArticleDetailView(DetailView):
	model = Post
	template_name = 'blog_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields =('title', 'title_tag', 'body')

class EditPostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'edit_post.html'
	#fields =('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('article_list')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields =('title', 'title_tag', 'body')

#class CategoryListView(ListView):
#	model = Post
#	template_name = 'category_list.html'

