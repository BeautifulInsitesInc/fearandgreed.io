from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone 


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name="Category")

	def __str__(self):
		return self.name
		# so that results can be seen when they are returned

	def get_absolute_url(self):
		#return reverse('article_list', args=(str(self.id)))
		return reverse('article_list')

class Post(models.Model):
	created_at = models.DateField(auto_now_add=True, verbose_name="Created at")
	updated_at = models.DateField(auto_now=True, verbose_name="Updated at")
	title = models.CharField(max_length=255, verbose_name="Title")
	title_tag = models.CharField(max_length=255, verbose_name="Title Tag")
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,verbose_name="Category")
	#category = models.CharField(max_length=255, default="category")
	author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Author")
	body = models.TextField()
	snippet = models.TextField()
	

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('article_detail', args=(str(self.id)))
		#return reverse('home')

