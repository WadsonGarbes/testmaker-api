from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("title", "text", "author", "created_at")