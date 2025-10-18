from django.test import TestCase
from home.forms import UserRegisterForm
from django.contrib.auth.models import User

class TestRegistrationForm(TestCase):

    @classmethod
    def setUpTestData(self):
        User.objects.create_user(username='kevin', email='kevin@gmail.com', password='kevin')

    def test_valid_data(self):
        form=UserRegisterForm(data={'username': 'jack', 'email': 'jack@gmail.com', 'password1': 'jack', 'password2': 'jack'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegisterForm(data={'username': '', 'email': '', 'password1': '', 'password2': ''})
        self.assertFalse(form.is_valid())

    def test_exit_email(self):
        form = UserRegisterForm(data={'username': 'kevin2', 'email': 'kevin@gmail.com', 'password1': 'kevin', 'password2': 'kevin'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))

    def test_unmached_password(self):
        form = UserRegisterForm(data={'username': 'kevin2', 'email': 'kevin@gmail.com', 'password1': 'kevin', 'password2': 'kevinnn'})
        self.assertEqual(len(form.errors), 2)
        self.assertTrue(form.has_error)

