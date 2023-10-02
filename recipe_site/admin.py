# from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
# from .models import Post, Comment


# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     list_display = ('recipe_name', 'slug', 'status', 'posted_on')
#     search_fields = ['recipe_name']
#     prepopulated_fields = {'slug': ('recipe_name', )}
#     list_filter = ('status', 'posted_on')
#     summernote_fields = ('ingredients', 'recipe_steps',)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):

#     list_display = ('name', 'body', 'post', 'posted_on')
#     search_fields = ('name', 'email', 'body')
#     list_filter = ('name', 'posted_on')
