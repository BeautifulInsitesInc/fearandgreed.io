from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import AddPostForm, EditPostForm, EditCategoryForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# -- ARTICLE VIEWS

class BlogHome(ListView):
	model = Post
	template_name = 'blog.html'
	cat_menu = Category.objects.all()
	ordering = ['-created_at']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(BlogHome, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class PostListView(ListView):
	model = Post
	template_name = 'post_list.html'
	ordering = ['-created_at']

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView, self).get_context_data()
		
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True


		context["cat_menu"]= cat_menu
		context["total_likes"]= total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields =('title', 'title_tag', 'body')

class AddPostView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields =('title', 'title_tag', 'body')


class EditPostView(UpdateView):
	model = Post
	form_class = EditPostForm
	template_name = 'edit_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('post_list')


# --- CATEGORY VIEWS ----------

def CategoryView(request, category_name):
	category_posts = Post.objects.filter(category__name__iexact=category_name.replace('-',' '))
	return render(request, 'category_page.html', {'category_name': category_name.title().replace('-',' '), 'category_posts':category_posts})

def CategoryListView(request):
	return render(request, 'category_list.html', {})

# ---- ADMIN CATEGORIES -------------------

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	success_url = reverse_lazy('category_list')

class EditCategoryView(UpdateView):
	model = Category
	form_class = EditCategoryForm
	template_name = 'edit_category.html'
	#fields = ['name']
	success_url = reverse_lazy('category_list')

class DeleteCategoryView(DeleteView):
	model = Category
	template_name = 'delete_category.html'
	#fields =('title', 'title_tag', 'body')
	#fields = '__all__'
	success_url = reverse_lazy('category_list')

# --- LIKE POST BUTTONS ------------------

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))

# ------- COMMENT SECTION -------------------------

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):  
		form.instance.post.id = self.kwargs['pk']
		return super().form_valid(form)
