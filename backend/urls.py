from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ? to use admin page:
    path("admin/", admin.site.urls),
    # ? Auth / djoser (use all the url's in the api.url):
    path("api/", include("api.urlsApi")),
]
