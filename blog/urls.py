from django.urls import path
from . import views


urlpatterns = [
    path('', views.globe_gazette, name='globe_gazette'),
]