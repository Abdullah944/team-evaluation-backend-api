from django.urls import path, include

# ? APPS:
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

# ? semester
router = SimpleRouter()
router.register("semester", SemesterViewSet)
# ? project
router.register("project", ProjectViewSet)
# ? team
router.register("team", TeamViewSet)
# ? Criteria
router.register("criteria", CriteriaViewSet)
# ? Evaluation
router.register("evaluation", EvaluationViewSet)
# ? Judge
router.register("judge", JudgeViewSet)

urlpatterns = [
    # ? Auth / djoser:
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    # ? semester / project / team / criteria:
    path("", include(router.urls)),
]
