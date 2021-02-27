from django.contrib import admin
from .models import Post,Advertise

# Register your models here.




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','description','updated','created')
	list_filter=('title','slug')
	prepopulated_fields={'slug':('title',)}



admin.site.register(Advertise)