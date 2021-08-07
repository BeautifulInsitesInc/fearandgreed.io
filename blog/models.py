from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone 
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name="Category Name")

	def __str__(self):
		return self.name
		# so that results can be seen when they are returned

	def get_absolute_url(self):
		return reverse('category_list', args=(str(self.id)))
		#return reverse('post_list')


class Profile(models.Model):
	#Associate with user model 1 to 1
	user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True,upload_to="images/profile",default='imgaes/default_profile.jpg')
	website_url = models.URLField(max_length=255, null=True, blank=True)
	twitter_url = models.URLField(max_length=255, null=True, blank=True)
	facebook_url = models.URLField(max_length=255, null=True, blank=True)
	pinterest_url = models.URLField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		#return reverse('home', args=(str(self.id)))
		return reverse('home')


class Post(models.Model):
	created_at = models.DateField(auto_now_add=True, verbose_name="Created at")
	updated_at = models.DateField(auto_now=True, verbose_name="Updated at")
	header_image = models.ImageField(null=True, blank=True,upload_to="images/")
	title = models.CharField(max_length=255, verbose_name="title")
	title_tag = models.CharField(max_length=255, verbose_name="title Tag")
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,verbose_name="Category")
	#author = models.ForeignKey(User, on_delete=models.SET_NULL,verbose_name="Author")
	author = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Author")
	#body = models.TextField()
	body = RichTextField(blank=True, null=True)
	snippet = models.TextField()
	#snippet = RichTextField(blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='blog_post')

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('post_list', args=(str(self.id)))
		return reverse('post_detail', args=(str(self.id)))

	def total_likes(self):
		return self.likes.count()


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	created_date = models.DateField(auto_now_add=True, verbose_name="created_date")
	updated_date = models.DateField(auto_now=True, verbose_name="updated_date")
	name = models.CharField(max_length=255, verbose_name="name")
	body = models.TextField()
	
	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

