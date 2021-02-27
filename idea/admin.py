from django.contrib import admin
from .models import Idea,Multimedia

# Register your models here.

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
	list_display=('author','title','photo','description')
	list_filter=('author','title')

admin.site.register(Multimedia)