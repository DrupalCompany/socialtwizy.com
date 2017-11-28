from django.contrib import admin

from .models import Group, Posts


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class PostsAdmin(admin.ModelAdmin):
    list_display = ['group','body']






admin.site.register(Group,GroupAdmin)
admin.site.register(Posts,PostsAdmin)
