from django.urls import path
from . import views


urlpatterns = [
    path("", views.AboutDetailView.as_view(), name="about_page"),
]