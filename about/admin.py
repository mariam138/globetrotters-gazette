from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(About, AboutAdmin)