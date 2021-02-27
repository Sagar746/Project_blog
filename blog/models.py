from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

POST_CHOICES=(
	('C','Country'),
	('P','Politics'),
	('E','Economy'),
	('H','Health'),
	('T','Tourism'),
	('Ed','Education'),
	('S','Sports')
)

class Post(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	description=models.TextField()
	image=models.ImageField(upload_to='post',blank=True)
	category=models.CharField(max_length=200,choices=POST_CHOICES,null=True)
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)

	# def save(self,*args,**kwargs):
	# 	self.slug=slugify(self.title)
	# 	super(Post, self).save(*args, **kwargs)

	class Meta:
		ordering=('-created',)

	def __str__(self):
		return self.title


class Advertise(models.Model):
	name=models.CharField(max_length=100)
	ads=models.ImageField(upload_to='advertise',null=True)

	def __str__(self):
		return self.name


