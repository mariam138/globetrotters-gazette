from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile

# add summernote to Profile bio text field in admin panel
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Profile, ProfileAdmin)