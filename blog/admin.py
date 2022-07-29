from django.contrib import admin
from blog.models import post


# Register your models here
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinymce.js',)