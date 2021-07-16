from django import forms
from .models import Post

#Create querry list
#categorylist = Category.objects.all().values_list('name','name')
#cat_list = []
#for item in categorylist:
#	cat_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'col-12 form-group'}),
			'title_tag': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
			'author': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			#'category': forms.Select(choices = cat_list, attrs={'class': 'col-md-6 form-group'}),
			'body': forms.Textarea(attrs={'class': 'col-12 form-group'}),
			'snippet': forms.Textarea(attrs={'class': 'col-12 form-group'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'col-12 form-group'}),
			'title_tag': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
			'category': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			'author': forms.Select(attrs={'class': 'col-md-6 form-group'}),
			#'category': forms.Select(choices = cat_list, attrs={'class': 'col-md-6 form-group'}),
			'body': forms.Textarea(attrs={'class': 'col-12 form-group'}),
			'snippet': forms.Textarea(attrs={'class': 'col-12 form-group'}),
		}