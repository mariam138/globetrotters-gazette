from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("asia/", views.AsiaPostList.as_view(), name="asia_posts"),
    path("africa/", views.AfricaPostList.as_view(), name="africa_posts"),
    path("australasia/", views.AusPostList.as_view(), name="australasia_posts"),
    path("europe-uk/", views.EuropePostList.as_view(), name="europe_posts"),
]