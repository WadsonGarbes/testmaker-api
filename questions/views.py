from rest_framework import generics, permissions

from .models import Question
from .serializers import QuestionSerializer
from .permissions import IsAuthorOrReadOnly


class QuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer