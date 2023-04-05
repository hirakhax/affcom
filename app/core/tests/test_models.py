from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def test_create_user_success(self):
        username = "user1"
        email = "user1@email.com"
        password = "password"
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_fail(self):
        username = "user1"
        password = "password"

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username=username,
                password=password,
            )

    def test_create_superuser_success(self):
        username = "user1"
        email = "user1@email.com"
        password = "password"
        user = get_user_model().objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.assertTrue(user.is_superuser)
