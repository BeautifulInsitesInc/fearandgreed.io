from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def category_list(request):
#   #categories = Category.objects.all()
#    return render (request, 'blog/category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

class BlogHome(ListView):
	model = Post
	template_name = 'blog.html'
	ordering = ['-created_at']

	# Function for passing category list to menu
	def get_context_date(self, *args, **kwargs):
		category_menu = Category.objects.all #contains the category list library, now push it to the page as a context dictionary that we can access
		context = super(BlogHome, self).get_context_data(*args, **kwargs)
		context["category_menu"] = category_menu
		return context

class ArticleListView(ListView):
	model = Post
	template_name = 'blog_list.html'
	ordering = ['-created_at']

def CategoryView(request, category_name):
	category_posts = Post.objects.filter(category__name__iexact=category_name.replace('-',' '))
	return render(request, 'categories.html', {'category_name': category_name.title().replace('-',' '), 'category_posts':category_posts})
	
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

