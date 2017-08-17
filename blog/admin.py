from django.contrib import admin
from .models import Post, Tag, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'author')
    search_fields = ('title',)
    ordering = ['created_time', 'modified_time']
    list_filter = ('created_time', 'modified_time', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
