from django.db import models

# Create your models here.

class Idea(models.Model):
	author=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	description=models.TextField()
	photo=models.ImageField(upload_to='Idea',null=True)
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author


class Multimedia(models.Model):
	title=models.CharField(max_length=100,null=True,blank=True)
	video=models.URLField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.title