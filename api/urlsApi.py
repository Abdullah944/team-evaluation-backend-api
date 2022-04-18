from django.urls import path, include
from semester.viewsSemester import SemesterViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("semester", SemesterViewSet)

urlpatterns = [
    # ? Auth / djoser:
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    # ? semester:
    path("", include(router.urls)),
]
# make migration + magrate:
