from django.contrib import admin
from .models import Task, Post

# Register your models here.

admin.site.register(Task)

class PostAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        
        # if object exists and content isnt checked, remove the description box
        if obj and not obj.content:
            fields.remove('description')
        
        return fields

admin.site.register(Post, PostAdmin)