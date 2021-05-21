from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase,APIClient
from .models import *
import json


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


class TestDossierMethods(APITestCase):
    def setUp(self):
        self.url = reverse('dossier')
        self.client = APIClient()
        self.user = User.objects.create_user(username='ismailov_atai',password='123456')
        self.dossier = Dossier.objects.create(user=self.user,fullname='Atai Ismailov',date_birth='2021-05-10',
                                              gender='M',
                                              )
        Car.objects.create(dossier=self.dossier,mark='hhgjg',model='dfgg',
                           year='2021-05-10',number='4',color='egdh',type='fghrt')

    def test_dossier_put_ok(self):
        self.client.login(username='ismailov_atai',password='123456')
        data = {
                "id": 4,
                "fullname": "Atai Ismailov",
                "image": "/sway_Hf4xU4t.jpeg",
                "user": 1,
                "date_birth": "2021-05-10",
                "gender": "M",
                "cars":  [
                        {
                            "car_id": 1,
                            "mark": "hhgjg",
                            "model": "dfgd",
                            "year": "2021-05-10",
                            "number": 4,
                            "color": "egdh",
                            "type": "fghrt"
                        }
                    ]
                }
        self.response = self.client.put(self.url,data=data,format='json')
        print(self.response.json())
        self.assertEqual(self.response.status_code,status.HTTP_200_OK)

    def test_delete(self):
        self.client.login(username='ismailov_atai', password='123456')
        self.response = self.client.delete(self.url)
        print(self.response.json())
        self.assertEqual(self.response.status_code,status.HTTP_200_OK)





