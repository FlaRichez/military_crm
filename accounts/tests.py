from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase,APIClient


class TestAccountAuth(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        User.objects.create_user(username='ismailov_atai',password='12345678')

    def test_account_auth(self):
        data = {
            'username':'ismailov_atai',
            'password':'12345678',
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,status.HTTP_200_OK)

    def test_account_not_auth(self):
        data = {
            'username':'ismailov_atai',
            'password':'1234567800'
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_auth(self):
        data = {
            'username':'ismailov_a99tai',
            'password':'12345678'
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,status.HTTP_400_BAD_REQUEST)




