from django.contrib import admin
from main.models import Project, Category, Post

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Post)