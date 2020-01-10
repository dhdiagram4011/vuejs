from django.contrib import admin

from .models import Todo

class TodoAmdin(admin.ModelAdmin):
    list_display = ['title','completed']

admin.site.register(Todo,TodoAmdin)



