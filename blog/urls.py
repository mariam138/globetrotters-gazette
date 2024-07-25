from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("<str:region>/", views.PostList.as_view(), name="region_posts")
]