from django import forms
from blog.models import Post



class PostCreateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','description','category','image']

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','description','category','image']
