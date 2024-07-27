from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Prepopulates the slug field from the post's title
    prepopulated_fields = {"slug": ("title",),}
    # Allows searching by title and country
    search_fields = ['title', 'country']
    # Displays certain fields of model
    list_display = ('title','country', 'user', 'created_on', 'status', 'approved',)
    # Chooses which fields to use as filtering
    list_filter = ('status', 'approved',)

# Register the Summernote editor for the admin console
@admin.register(PostAdmin)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register your models here.
