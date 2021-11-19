import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import Task
# Create your tests here.

class ForgotPasswordTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )

    def test_forgotpassword(self):

        url = '/api/password_reset/'
        data = {
            "email" : "test@gmail.com"
        }
        req = self.client.post(url, data)

        data2 = {
            "email" : "test2@gmail.com"
        }
        req2 = self.client.post(url, data2)


        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req2.status_code, status.HTTP_400_BAD_REQUEST)


    def test_resetpassword(self):
        url = '/api/password_reset/'
        data = {
            "email": "test@gmail.com"
        }
        req = self.client.post(url, data)
        print(req)
        self.assertEqual(req.status_code, status.HTTP_200_OK)


class RegistrationTestCase(APITestCase):
    """
    Test User Registration In different cases.
    """
    def test_registration(self):
        data = {
            'first_name': 'test',
            'last_name' : 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': 'Test_user_password_123',
        }
        data1 = {
            'first_name': 'test',
            'last_name' : 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': '123',
        }

        url = '/register/'
        response1 = self.client.post(url, data)
        response2 = self.client.post(url, data)
        response3 = self.client.post(url, data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)


class LoginUserTestCase(APITestCase):
    """
    Test login api with valid and invalid credentials.
    """
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@test.com',
            username='test',
            password='test'
        )
    def test_login_user(self):
        url = '/login/'
        data = {
            'username' : 'test',
            'password' : 'test'
        }
        data2 = {
            'username': 'test',
            'password': 'tes'
        }
        response1 = self.client.post(url, data)
        response2 = self.client.post(url, data2)

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)


class CreateTaskCases(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )

    def test_createtask(self):
        user = self.user
        self.client.login(username='test', password="test")
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.token = refresh.access_token

        data = {
            "task_title": "test",
            "task_description": "test",
            "is_complete": False,
            "task_category": "Home Task",
            "task_start_date": "2021-11-19T12:02:48.267Z",
            "task_end_date": "2021-11-19T12:02:48.267Z",
        }
        url = '/tasks/'

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

