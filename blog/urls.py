from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("asia/", views.AsiaPostList.as_view(), name="asia_posts"),
    path("africa/", views.AfricaPostList.as_view(), name="africa_posts"),
    path("australasia/", views.AusPostList.as_view(), name="australasia_posts"),
    path("europe-uk/", views.EuropePostList.as_view(), name="europe_posts"),
    path("middle-east/", views.MenaPostList.as_view(), name="mena_posts"),
    path("south-america/", views.SAmericaPostList.as_view(), name="sa_posts"),
    path("north-america/", views.NAmericaPostList.as_view(), name="us_posts"),
    # path("search/",)
]