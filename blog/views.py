from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from idea.models import Idea
from .forms import(
	PostCreateForm,
	PostUpdateForm,
	IdeaCreateForm,
	IdeaUpdateForm,
)

from django.contrib.auth.decorators import login_required

from idea.models import Multimedia

# Create your views here.

def post_home(request):
	posts=Post.objects.all()[:4]
	post_national=Post.objects.filter(category='C')[1:7]
	post_political=Post.objects.filter(category='P')[:6]
	post_economy=Post.objects.filter(category='E')[:6]
	post_education=Post.objects.filter(category='Ed')[:6]
	post_health=Post.objects.filter(category='H')[:6]
	post_tourism=Post.objects.filter(category='T')[:6]
	

	context={
	'posts':posts,
	# 'post_filter':post_filter,
	'post_national':post_national,
	'post_political':post_political,
	'post_economy':post_economy,
	'post_education':post_education

	}
	return render(request,'home.html',context)

def home_detail(request,id): 
	posts=Post.objects.filter(id=id)
	latest_news=Post.objects.all()[:5]
	context={
	'posts':posts,
	'latest_news':latest_news
	}
	return render(request,'details/detail.html',context)


def nation(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='C')[:1]
	posts_filter=Post.objects.filter(category='C')[1::]
	ideas=Idea.objects.all()[:4]
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'nation.html',context)

def nation_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='C',id=id)
	# posts=Post.objects.filter(category='P',id=id)
	# posts=Post.objects.filter(category='H',id=id)
	# posts=Post.objects.filter(category='E',id=id)
	# posts=Post.objects.filter(category='Ed',id=id)
	# posts=Post.objects.filter(category='T',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)


def politics(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='P')[:1]
	posts_filter=Post.objects.filter(category='P')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'politics.html',context)

def politics_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='P',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)


def economy(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='E')[:1]
	posts_filter=Post.objects.filter(category='E')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas

	}
	return render(request,'economy.html',context)

def economy_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='E',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)


def tourism(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='T')[:1]
	posts_filter=Post.objects.filter(category='T')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'tourism.html',context)

def tourism_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='T',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)

def health(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='H')[:1]
	posts_filter=Post.objects.filter(category='H')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'health.html',context)

def health_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='H',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)

def education(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='Ed')[:1]
	posts_filter=Post.objects.filter(category='Ed')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'education.html',context)


def education_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='Ed',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)

def sports(request):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='S')[:1]
	posts_filter=Post.objects.filter(category='S')[1::]
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'posts_filter':posts_filter,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'sports.html',context)

def sports_detail(request,id):
	latest_news=Post.objects.all()[:5]
	posts=Post.objects.filter(category='Ed',id=id)
	ideas=Idea.objects.all()
	context={
	'posts':posts,
	'latest_news':latest_news,
	'ideas':ideas
	}
	return render(request,'details/detail.html',context)




def idea(request):
	ideas=Idea.objects.all()
	context={
	'ideas':ideas
	}
	return render(request,'Idea/idea.html',context)

def idea_detail(request,id=id):
	idea=Idea.objects.get(id=id)
	context={
	'idea':idea
	}
	return render(request,'idea/idea_detail.html',context)



	#####################################



def post_create(request):
	form=PostCreateForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('blog:post_list')
	context={
	'form':form
	}
	return render(request,'admin/post_create.html',context)

@login_required
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
		return redirect('blog:post_list')
	context={
	'form':form
	}
	return render(request,'admin/post_create.html',context)

def post_delete(request,id):
	post=get_object_or_404(Post,id=id)
	post.delete()
	return redirect('blog:post_list')


	################

def idea_create(request):
	form=IdeaCreateForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		form.save()
	context={
	'form':form
	}
	return render(request,'admin/idea_create.html',context)


def idea_list(request):
	ideas=Idea.objects.all()
	context={
	'ideas':ideas
	}
	return render(request,'admin/idea_list.html',context)

def idea_edit(request,id):
	idea=get_object_or_404(Idea,id=id)
	form=IdeaUpdateForm(request.POST or None,request.FILES or None,instance=idea)
	if form.is_valid():
		form.save()
		return redirect('blog:idea_list')
	context={
	'idea':idea,
	'form':form
	}
	return render(request,'admin/idea_create.html',context)

def idea_delete(request,id):
	idea=get_object_or_404(Idea,id=id)
	idea.delete()
	return redirect('blog:idea_list')


@login_required
def admin(request):
	return render(request,'admin/admin.html')