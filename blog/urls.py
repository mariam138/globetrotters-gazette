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
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create-post/", views.create_post, name="create_post"),
    path("create-post/cancel", views.cancel_create_post, name="cancel_post"),
    path("post/<slug:slug>/edit", views.edit_post, name="edit_post"),
    path("post/<slug:slug>/cancel-edit", views.cancel_edit_post, name="cancel_post_edit"),
    path("post/<slug:slug>/delete", views.delete_post, name="delete_post"),
    path("<str:username>/posts/", views.UserPostList.as_view(), name="users_posts"),

]
