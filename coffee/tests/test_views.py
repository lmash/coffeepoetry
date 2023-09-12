from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Runs once"""
        cls.user = User.objects.create(username='testuser')
        cls.Client = Client()

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/login")
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)

    def test_register_user_available_from_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "coffee/login.html")
        self.assertContains(response, f'<a href="{reverse("register")}">Register here.</a>')


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Runs once"""
        cls.user = User.objects.create(username='testuser')
        cls.Client = Client()

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, 200)

    def test_menu_items_available_when_logged_out(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "coffee/index.html")
        self.assertContains(response, f'<a class="navbar-brand" href="{reverse("index")}">CoffeePoetry</a>')
        self.assertContains(response, f'<a class="nav-link" href="{reverse("login")}">Log In</a>')
        self.assertContains(response, f'<a class="nav-link" href="{reverse("register")}">Register</a>')
