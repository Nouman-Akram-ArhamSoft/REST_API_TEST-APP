"""This module is used to testing the API of todo_app"""
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


# Create your tests here.

class ForgotPasswordTestCase(APITestCase):
    """
    Test Class for testing the Forgot password API
    """

    def setUp(self) -> None:
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )

    def test_forgot_password(self) -> None:
        """
        Function used to test the forgot password API
        :return: None
        """
        url = '/api/password_reset/'
        data = {
            "email": "test@gmail.com"
        }
        req = self.client.post(url, data)

        data2 = {
            "email": "test2@gmail.com"
        }
        req2 = self.client.post(url, data2)

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req2.status_code, status.HTTP_400_BAD_REQUEST)


class RegistrationTestCase(APITestCase):
    """
    Test User registration in different cases.
    """

    def test_registration(self) -> None:
        """
        Function use to test the registration API
        :return: None
        """
        sample_data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': 'Test_user_password_123',
        }

        # Testing with short Password
        second_sample_data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': '123',
        }

        url = '/register/'

        first_registration_response = self.client.post(url, sample_data)

        same_registration_response = self.client.post(url, sample_data)

        short_password_response = self.client.post(url, second_sample_data)

        self.assertEqual(first_registration_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(same_registration_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(short_password_response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginUserTestCase(APITestCase):
    """
    Test login api with valid and invalid credentials.
    """

    def setUp(self) -> None:
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@test.com',
            username='test',
            password='test'
        )

    def test_login_user(self) -> None:
        """
        Test Login user API
        :return: None
        """
        url = '/login/'
        sample_data = {
            'username': 'test',
            'password': 'test'
        }
        wrong_sample_data = {
            'username': 'test',
            'password': 'tes'
        }
        response1 = self.client.post(url, sample_data)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        response2 = self.client.post(url, wrong_sample_data)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)


class CreateTaskTestCases(APITestCase):
    """
    Test Create Task API.
    """

    def setUp(self) -> None:
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )
        url = reverse('login')
        resp = self.client.post(url, {'username': 'test', 'password': 'test'}, format='json')
        self.token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {self.token}'
        }

        self.data = {
            "task_title": "test",
            "task_description": "test",
            "is_complete": False,
            "task_category": "Home Task",
            "task_start_date": "2021-11-19T12:02:48.267Z",
            "task_end_date": "2021-11-19T12:02:48.267Z"
        }

    def test_create_task(self) -> None:
        """
        Test create Task API
        :return: None
        """
        url = '/tasks/'
        post_response = self.client.post(path=url, data=self.data, **self.headers)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)


class DeleteTaskTestCases(APITestCase):
    """Class used for testing the Delete Task API"""

    def setUp(self) -> None:
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )
        url = reverse('login')
        resp = self.client.post(url, {'username': 'test', 'password': 'test'}, format='json')
        self.token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {self.token}'
        }

        self.task_obj = Task(
            task_title='test2',
            task_description='test2',
            is_complete=False,
            task_category='Home Task',
            task_start_date='2021-11-19T12:02:48.267Z',
            task_end_date='2021-11-19T12:02:48.267Z',
            person=self.user
        )
        self.task_obj.save()

        self.test_task_obj = Task(
            task_title='test2',
            task_description='test2',
            is_complete=False,
            task_category='Home Task',
            task_start_date='2021-11-19T12:02:48.267Z',
            task_end_date='2021-11-19T12:02:48.267Z',
            person=self.user
        )
        self.test_task_obj.save()

    def test_soft_delete_task(self) -> None:
        """
        Soft Delete API Testing
        :return: None
        """
        url = f"/soft_delete/{self.test_task_obj.pk}/"
        get_response = self.client.delete(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task(self) -> None:
        """
        Test Delete Task API
        :return: None
        """
        url = f'/tasks/{self.task_obj.pk}/'
        get_response = self.client.delete(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_204_NO_CONTENT)


class CRUDTaskTestCases(APITestCase):
    """
    Test get Task, get specific task,
    update task and update specific task.
    """

    def setUp(self) -> None:
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )
        url = reverse('login')
        resp = self.client.post(url, {'username': 'test', 'password': 'test'}, format='json')
        self.token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {self.token}'
        }

        self.task = Task(
            task_title='test',
            task_description='test',
            is_complete=False,
            task_category='Home Task',
            task_start_date='2021-11-19T12:02:48.267Z',
            task_end_date='2021-11-19T12:02:48.267Z',
            person=self.user
        )
        self.task.save()

    def test_get_tasks(self) -> None:
        """
        Test get Tasks API
        :return: None
        """
        url = '/tasks/'
        get_response = self.client.get(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_get_specific_tasks(self) -> None:
        """
        Test get specific Tasks API
        :return: None
        """

        url = f'/tasks/{self.task.pk}/'
        get_response = self.client.get(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        # testing with invalid Task ID
        url = f'/tasks/{10}/'
        get_response = self.client.get(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_tasks(self) -> None:
        """
        Test Update Task API
        :return: None
        """
        url = f"/tasks/{self.task.pk}/"
        test_data = {
            "task_title": "updated test",
            "task_description": "updated test",
            "is_complete": True,
            "task_category": "Home Task",
            "task_start_date": "2021-11-22T12:53:32.910Z",
            "task_end_date": "2021-11-22T12:53:32.910Z"
        }

        update_response = self.client.put(path=url, data=test_data, **self.headers)
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

    def test_partial_update_task(self) -> None:
        """
        Test partial Update Task API
        :return: None
        """
        url = f"/tasks/{self.task.pk}/"
        test_data = {
            "task_title": "Partial updated test"
        }

        partial_update_response = self.client.patch(path=url, data=test_data, **self.headers)
        self.assertEqual(partial_update_response.status_code, status.HTTP_200_OK)


class ShowUserTestCases(APITestCase):
    """Class used for testing the Show Profile API"""

    def setUp(self):
        """
        Setup the object for testing the API
        :return: None
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test'
        )
        url = reverse('login')
        resp = self.client.post(url, {'username': 'test', 'password': 'test'}, format='json')
        self.token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {self.token}'
        }

    def test_show_user_profile(self) -> None:
        """
        Test Show User Profile API
        :return: None
        """
        url = "/show_profile/"

        partial_update_response = self.client.get(path=url, **self.headers)
        self.assertEqual(partial_update_response.status_code, status.HTTP_200_OK)
