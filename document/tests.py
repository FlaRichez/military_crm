from django.contrib.auth.models import User,Group
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase,APIClient
from .factory import populate_test_db_docs,populate_test_db_users
from .models import Document


class TestDocumentRulesGet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        # create user and group
        populate_test_db_users(User,Group)
        # create docs for users
        populate_test_db_docs(Document)

    def test_sergeant_permissions(self):
        self.client.login(username='sergeant',password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='private doc', status_code=200)

    def test_document_create(self):
        self.client.login(username='general', password='123456')
        data = {
            "title":'gogo',
            'status':'active',
            'text':'1223',
            'data_expired':'2020-06-06',
            'document_root':'public'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_document_no_create_sergeant(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            'title':'ogogo',
            'status':'active',
            'text':'1223',
            'data_expired':'2020-06-06',
            'document_root':'secret'
        }
        self.response = self.client.post(self.url,data)
        self.assertNotEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_document_create_president(self):
        self.client.login(username='president', password='123456')
        data = {
            "title":'ogogo',
            'status':'active',
            'text':'1223',
            'data_expired':'2020-06-06',
            'document_root':'top-secret'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_document_createe_president(self):
        self.client.login(username='president', password='123456')
        data = {
            'title':'ogogo',
            'status':'active',
            'text':'1223',
            'data_expired':'2020-06-06',
            'document_root':'private'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_president_create_error(self):
        self.client.login(username='president', password='123456')
        data = {
            'title':'presidentahaha',
            'status':'active',
            'text':'ogogokg',
            'data_expired':'2021-05-14',
            'document_root':'top-secret'
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)


class TestDataExpiredDocument(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.doc1 = Document.objects.create(title='not expired doc',
                                data_expired="2021-05-22",document_root='private')
        self.doc2 = Document.objects.create(title='expired doc',
                                data_expired="2021-05-09",document_root='private',status='dead')
        populate_test_db_users(User, Group)

    def test_get_not_expired(self):
        self.url = reverse('documents-detail',kwargs={'pk':self.doc1.id})
        self.client.login(username='general',password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response,'active',status_code=200)

    def test_get_expired(self):
        self.url = reverse('documents-detail', kwargs={'pk': self.doc2.id})
        self.client.login(username='general',password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response,'Страница не найдена',status_code=404)









