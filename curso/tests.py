from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from curso.models import Curso

class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso de teste', nivel_curso='B'
        )

        url_login = reverse('login')
        UserModel = get_user_model()
        self.user_1 = UserModel.objects.create_user(
            username='user_teste', password='teste@123'
        )
        response = self.client.post(url_login, {
            'username': 'user_teste', 'password': 'teste@123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.token = response.data['token']


    def test_getall(self):
        """Teste listagem de cursos"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_getone(self):
        """Teste para listar um unico curso"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        """Teste cadastro de curso"""
        data = {
            'codigo_curso': 'CTT2',
            'descricao': 'Curso de teste 2',
            'nivel_curso': 'B'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delet(self):
        """Teste update do curso curso"""
        data = {
            'codigo_curso': 'CTT1Put',
            'descricao': 'Curso de teste',
            'nivel_curso': 'B'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch(self):
        """Teste update via patch do curso curso"""
        data = {
            'codigo_curso': 'CTT1Patch'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.patch('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)