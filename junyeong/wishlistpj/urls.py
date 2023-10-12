from django import views
from django.contrib import admin
from django.urls import path, include
import wishlistapp.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", wishlistapp.views.index, name="index"),
    path("new/", wishlistapp.views.new, name="new"),
    path("new/create/", wishlistapp.views.create, name="create"),
    path(
        "read/",
        wishlistapp.views.read,
        name="read",
    ),
    path("mypost/", wishlistapp.views.mypost, name="mypost"),
    path("detail/<str:id>/", wishlistapp.views.detail, name="detail"),
    path("user/", include("userapp.urls")),
    path("whislist/", wishlistapp.views.wishlist, name="wishlist"),
    path(
        "add_to_wishlist/<str:post_id>/",
        wishlistapp.views.add_to_wishlist,
        name="add_to_wishlist",
    ),
    path(
        "remove_from_wishlist/<str:post_id>/",
        wishlistapp.views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
]
