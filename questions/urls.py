from django.urls import path

from .views import QuestionList, QuestionDetail

urlpatterns = [
    path("<int:pk>/", QuestionDetail.as_view(), name="question_detail"),
    path("", QuestionList.as_view(), name="question_list"),
]