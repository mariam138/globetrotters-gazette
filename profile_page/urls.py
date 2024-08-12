from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/", views.profile_page, name="profile_page"),
    path("<str:username>/edit", views.edit_save_profile, name="edit_profile"),
    path(
        "<str:username>/cancel",
        views.edit_cancel_profile, name="cancel_profile_changes"),
    path("<str:username>/delete", views.delete_account, name="delete_account"),

]
