from django.urls import path, include
from semester.viewsSemester import SemesterViewSet
from project.viewsProject import ProjectViewSet
from team.viewsTeam import TeamViewSet
from rest_framework.routers import (
    SimpleRouter,
)  # ?you have to use it for the modal in the view & without / at th end

# semester
router = SimpleRouter()
router.register("semester", SemesterViewSet)
# project
router.register("project", ProjectViewSet)
# team
router.register("team", TeamViewSet)

urlpatterns = [
    # ? Auth / djoser:
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    # ? semester / project / team:
    path("", include(router.urls)),
]
