from django.core.cache import cache
from http import HTTPStatus
from django.test import TestCase, Client
from ..models import Post, Group, User, Comment


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="HasNoName")
        cls.group = Group.objects.create(
            title="Тестовая группа",
            slug="test-slug",
            description="Тестовое описание",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text="Тестовый пост",
        )
        cls.comment = Comment.objects.create(
            author=cls.user,
            text="Тестовый комментарий",
        )

    def setUp(self):
        cache.clear()
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(PostURLTests.user)

    def test_url_exists_at_desired_location(self):
        """Страница url доступна любому пользователю."""
        urlpatterns = ['/', f'/group/{self.group.slug}/',
                       f'/profile/{self.post.author}/',
                       f'/posts/{self.post.id}/']
        for url in urlpatterns:
            response = self.guest_client.get(url)
            self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_unexisting_page_exists_at_desired_location(self):
        """Страница unexisting_page не доступна любому пользователю."""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, 404)

    def test_post_create_url_exists_at_desired_location(self):
        """Страница create/ доступна авторизованному пользователю."""
        response = self.authorized_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_post_edit_url_exists_at_desired_location_authorized(self):
        """Страница posts/<post_id>/edit/ доступна авторизованному
        пользователю."""
        response = self.authorized_client.get(f'/posts/{self.post.id}/edit/')
        self.assertEqual(response.status_code, 200)

    def test_post_comment_url_exists_at_desired_location_authorized(self):
        """Страница posts/<int:post_id>/comment/ доступна авторизованному
        пользователю."""
        response = self.authorized_client.get(
            f'/posts/{self.post.id}/comment/'
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/': 'posts/index.html',
            f'/group/{self.group.slug}/': 'posts/group_list.html',
            f'/profile/{self.post.author}/': 'posts/profile.html',
            f'/posts/{self.post.id}/': 'posts/post_detail.html',
            '/create/': 'posts/create_post.html',
            f'/posts/{self.post.id}/edit/': 'posts/create_post.html'
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)
