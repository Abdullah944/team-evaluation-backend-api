from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # ? Auth / djoser:
    path("api/", include("api.urlsApi")),
]
