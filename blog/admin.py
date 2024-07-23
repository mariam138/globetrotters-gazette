from django.contrib import admin
from .models import Post

# Prepopulates the slug field from the post's title
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Post)