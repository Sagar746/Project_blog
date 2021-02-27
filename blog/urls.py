from django.urls import path
from .views import(
	post_home,
	home_detail,
	nation,
	nation_detail,
	politics,
	politics_detail,
	economy,
	economy_detail,
	tourism,
	tourism_detail,
	health,
	health_detail,
	education,
	education_detail,
	sports,
	sports_detail,
	
	
	idea,
	idea_detail,

	# POST CRUD STARTS
	post_create,
	post_list,
	post_edit,
	post_delete,
	
	# POST CRUD ENDS

	idea_create,
	idea_list,
	idea_edit,
	idea_delete,

	admin
)

app_name='blog'
urlpatterns=[
	path('',post_home,name='post_home'),
	path('home_detail/<int:id>/',home_detail,name='home_detail'),

	path('nation/',nation,name='nation'),
	path('nation_detail/<int:id>/',nation_detail,name='nation_detail'),

	path('politics/',politics,name='politics'),
	path('politics_detail/<int:id>/',politics_detail,name='politics_detail'),

	path('economy/',economy,name='economy'),
	path('economy_detail/<int:id>/',economy_detail,name='economy_detail'),

	path('tourism/',tourism,name='tourism'),
	path('tourism_detail/<int:id>/',tourism_detail,name='tourism_detail'),

	path('health/',health,name='health'),
	path('health_detail/<int:id>/',health_detail,name='health_detail'),

	path('education/',education,name='education'),
	path('education_detail/<int:id>/',education_detail,name='education_detail'),

	path('sports/',sports,name='sports'),
	path('sports_detail/<int:id>/',sports_detail,name='sports_detail'),

	path('idea/',idea,name='idea'),
	path('idea_detail/<int:id>/',idea_detail,name='idea_detail'),


	path('economy_detail/<int:id>/',economy_detail,name='economy_detail'),

	
	path('post_create/',post_create,name='post_create'),
	path('post_list/',post_list,name='post_list'),
	path('post_edit/<int:id>/',post_edit,name='post_edit'),
	path('post_delete/<int:id>/',post_delete,name='post_delete'),

	path('idea_create/',idea_create,name='idea_create'),
	path('idea_list/',idea_list,name='idea_list'),
	path('idea_edit/<int:id>/',idea_edit,name='idea_edit'),
	path('idea_delete/<int:id>/',idea_delete,name='idea_delete'),
	path('myadmin/',admin,name='admin'),
	

]