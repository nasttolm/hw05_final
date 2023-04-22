from django.test import TestCase
from ..models import Group, Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )
        cls.comment = Comment.objects.create(
            author=cls.user,
            text="Тестовый комментарий",
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        post = PostModelTest.post
        group = PostModelTest.group
        expected_object_name = {
            post: post.text[:15],
            group: group.title
        }
        for model, object_name in expected_object_name.items():
            with self.subTest(model=model):
                self.assertEqual(object_name, str(model))
