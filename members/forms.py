from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import User
from django import forms
from blog.models import Profile

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'website_url', 'twitter_url', 'facebook_url', 'pinterest_url')
		
		widgets = {
				'bio': forms.Textarea(attrs={'class': 'col-12 form-group'}),
				#'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
				'website_url': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
				'twitter_url': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
				'facebook_url': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
				'pinterest_url': forms.TextInput(attrs={'class': 'col-md-6 form-group'}),
			}

class SignUpForm(UserCreationForm):
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'col-md-12 form-group'})),
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),

	class Meta:
		model = User
		fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['password2'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['last_name'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['first_name'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['email'].widget.attrs['class'] = 'col-md-12 form-group'


class EditProfileForm(UserChangeForm): #from views.py form_classs = 
	#get these field names by viewing source of edit profile page
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'col-md-12 form-group'})),
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'col-md-12 form-group'})),
	#is_superuser = forms.CheckboxInput(),
	is_staff = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	is_active = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'col-md-12 form-group'})),

	class Meta:
		model = User
		fields = ('username', 'last_name', 'first_name', 'email', 'last_login','is_superuser','is_staff','date_joined')
		#fields = ('username', 'last_name', 'first_name', 'email', 'last_login','password')
	
	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['first_name'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['email'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['password'].widget.attrs['class'] = 'col-md-12 form-group'
		self.fields['is_superuser'].widget.attrs['class'] = 'form-check'
		self.fields['is_staff'].widget.attrs['class'] = 'form-check'

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-md-12 form-group', 'type':'password'})),
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'col-md-12 form-group', 'type':'password'})),
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'col-md-12 form-group', 'type':'password'})),

	class Meta:
		model = User
		#fields = ('old_password', 'new_password1', 'new_password2')
		fields = ('old_password', 'new_password1')