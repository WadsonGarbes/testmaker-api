from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Question


class QuestionModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="12345")
        Question.objects.create(
            title="This is a test question",
            text="This is a test text",
            author=user,
        )

    def test_question_content(self):
        question = Question.objects.get(id=1)
        expected_author = f"{question.author}"
        expected_title = f"{question.title}"
        expected_text = f"{question.text}"
        self.assertEqual(expected_author, "testuser")
        self.assertEqual(expected_title, "This is a test question")
        self.assertEqual(expected_text, "This is a test text")
