from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


class PostAdmin(SummernoteModelAdmin):
    # Prepopulates the slug field from the post's title
    prepopulated_fields = {"slug": ("title",),}
    # Allows searching by title and country
    search_fields = ['title', 'country']
    # Displays certain fields of model
    list_display = ('title','country', 'user', 'created_on', 'status', 'approved',)
    # Chooses which fields to use as filtering
    list_filter = ('status', 'approved',)
    # Applies summernote editor to all Textfields
    summernote_fields = '__all__'

@admin.action(description="Mark selected comments approved")
def approve_comments(modeladmin, request, queryset):
    queryset.update(approved=True)

class CommentAdmin(admin.ModelAdmin):
    # Displays fields in admin panel
    list_display = ('user', 'post', 'body', 'approved',)
    # Chooses to filter comments by approval status
    list_filter = ('approved',)
    # Registers custom actions defined above
    actions = [approve_comments]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
