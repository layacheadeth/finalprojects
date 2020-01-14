from django.contrib import admin
#imported from the models inside the same directory so the database can be registered here
from .models import Post,blog
#what to show and what not to.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
#you can modify all the database through admin by register all the class you submit to database
admin.site.register(Post,PostAdmin)


from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
#database registration to admin
admin.site.register(Comment)
#reference:https://djangocentral.com/creating-comments-system-with-django/
admin.site.register(blog)