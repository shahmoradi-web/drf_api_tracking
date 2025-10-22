from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from home.forms import UserRegisterForm
from home.views import home


class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('home:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.failUnless(response.context['form'],UserRegisterForm)

    def test_user_register_POST_valid_data(self):
        data = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'strong_password_123',
            'password2': 'strong_password_123',
}
        response = self.client.post(reverse('home:register'),data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_done.html')
        self.assertEqual(User.objects.count(), 1)
        self.assertIn('user', response.context)

    def test_user_register_POST_invalid_data(self):
        data = {
            'username': 'testuser2',
            'email': 'test255@email',
            'password1': 'strong_password_1234',
            'password2': 'strong_password_1234',
        }
        response = self.client.post(reverse('home:register'),data=data)
        self.assertEqual(response.status_code, 200)    
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(form=response.context['form'],field='email',errors='Enter a valid email address.')

class TestHomeViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root', email='root@email.com', password='rootpass')
        self.factory = RequestFactory()

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse('home:home'))
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 302)

    def test_home_user_anonymous(self):
        request = self.factory.get(reverse('home:home'))
        request.user = AnonymousUser()
        response = home(request)
        self.assertEqual(response.status_code, 200)