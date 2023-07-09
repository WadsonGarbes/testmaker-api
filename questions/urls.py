from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, QuestionViewSet

router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("", QuestionViewSet, basename="questions")

urlpatterns = router.urls
