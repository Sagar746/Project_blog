from django import forms
from .models import Post
from idea.models import Idea



class PostCreateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','description','category','image']

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','description','category','image']



class IdeaCreateForm(forms.ModelForm):
	class Meta:
		model=Idea
		fields=['author','title','description','photo']


class IdeaUpdateForm(forms.ModelForm):
	class Meta:
		model=Idea
		fields=['author','title','description','photo']