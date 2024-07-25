from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("asia/", views.AsiaPostList.as_view(), name="asia_posts"),
    path("africa/", views.AfricaPostList.as_view(), name="africa_posts")
]