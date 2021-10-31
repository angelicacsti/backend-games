import json
import jwt

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class TestAPI(TestCase):
    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/user/', 
            {
                "username": "user_prueba_1",
                "password": "password_prueba_1",
                "name": "user prueba",
                "email": "user_prueba_1@misionTIC.com",
                "account": {
                "lastChangeDate": "2021-09-23T10:25:43.511Z",       
                "isActive": "true"
                }
        },
        format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)


