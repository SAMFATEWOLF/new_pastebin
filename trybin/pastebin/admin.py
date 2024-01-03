from django.contrib import admin
from .models import *


class NewPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'crt_time', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('crt_time', 'title', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)


admin.site.register(NewPost, NewPostAdmin)
admin.site.reister(Category, CategoryAdmin)
# Register your models here.
