from django import forms
from .models import Post, Category, Comment

#Create querry list
#categorylist = Category.objects.all().values_list('name','name')
#cat_list = []
#for item in categorylist:
#	cat_list.append(item)

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('header_image', 'title', 'title_tag', 'author', 'category', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'col-12 form-group'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			#'author': forms.TextInput(attrs={'class': 'col-md-6 form-group', 'placeholder': 'user name', 'id':'userid'}),
			'author': forms.TextInput(attrs={'class': 'col-md-6 form-group', 'value': 'user name', 'id':'userid', 'type':'hidden'}),
			#'author': forms.TextInput(attrs={'class': 'col-md-6 form-group', 'value': 'user name', 'id':'userid'}),
			#'category': forms.Select(choices = cat_list, attrs={'class': 'col-md-6 form-group'}),
			'body': forms.Textarea(attrs={'class': 'col-12 form-group'}),
			'snippet': forms.Textarea(attrs={'class': 'col-12 form-group'}),
		}

class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'col-12 form-group'}),
			'title_tag': forms.TextInput(),
			'category': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			#'author': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			#'category': forms.Select(choices = cat_list, attrs={'class': 'col-md-6 form-group'}),
			'body': forms.Textarea(attrs={'class': 'col-12 form-group'}),
			'snippet': forms.Textarea(attrs={'class': 'col-12 form-group'}),
		}

class EditCategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'col-12 form-group'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')
		
		widgets = {
				'name': forms.TextInput(attrs={'class': 'col-12 form-group'}),
				'body': forms.Textarea(attrs={'class': 'col-md-6 form-group'}),
		}