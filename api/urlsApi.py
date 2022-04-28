from django.urls import path, include

# ? Views / controllers => functions:
from semester.viewsSemester import SemesterViewSet
from project.viewsProject import ProjectViewSet
from team.viewsTeam import TeamViewSet
from criteria.viewsCriteria import CriteriaViewSet
from evaluation.viewsEvaluation import EvaluationViewSet
from judge.viewsJudge import JudgeViewSet

# ? SimpleRouter
from rest_framework.routers import (
    SimpleRouter,
)  # ?you have to use it for the modal in the view & without / at th end

# ? declare Simple Router:
router = SimpleRouter()
# ? Semester Router:
router.register("semester", SemesterViewSet)
# ? Project Router:
router.register("project", ProjectViewSet)
# ? Team Router:
router.register("team", TeamViewSet)
# ? Criteria Router:
router.register("criteria", CriteriaViewSet)
# ? Evaluation Router:
router.register("evaluation", EvaluationViewSet)
# ? Judge
router.register("judge", JudgeViewSet)

urlpatterns = [
    # ? Auth / djoser:
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    # ? semester / project / team / criteria / evaluation/ judge => path's:
    path("", include(router.urls)),
]
