from django.shortcuts import render,redirect
from blog.models import Post
from .forms import PostCreateForm,PostUpdateForm


# Create your views here.
def post_create(request):
	form=PostCreateForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('post_list')
	context={
	'form':form
	}
	return render(request,'admin/post_create.html',context)

def post_list(request):
	posts=Post.objects.all()
	context={
	'posts':posts
	}
	return render(request,'admin/post_list.html',context)

def post_edit(request,id):
	post=get_object_or_404(Post,id=id)
	form=PostUpdateForm(request.POST or None,request.FILES or None,instance=post)
	if form.is_valid():
		post=form.save(commit=False)
		post.save()
		return redirect('post_list')
	context={
	'form':form
	}
	return render(request,'admin/post_create.html',context)

def post_delete(request,id):
	post=get_object_or_404(Post,id=id)
	post.delete()
	return redirect('post_list')