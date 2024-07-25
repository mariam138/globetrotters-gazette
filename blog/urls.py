from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("asia/", views.AsiaPostList.as_view(), name="asia_posts")
]