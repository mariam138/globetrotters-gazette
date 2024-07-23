from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Prepopulates the slug field from the post's title
    prepopulated_fields = {"slug": ("title",),}
    # Allows searching by title and country
    search_fields = ['title', 'country']
    # Displays certain fields of model
    list_display = ('title', 'created_on','status', 'approved',)
    # Chooses which fields to use as filtering
    list_filter = ('status', 'approved',)

# Register your models here.
