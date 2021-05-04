from django.test import TestCase
from curso.models import Curso
from curso.serializer import CursoSerializer

class CursoSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo_curso='CTT1', descricao='Curso de teste', nivel_curso='B'
        )
        self.serializer = CursoSerializer(instance=self.curso)

    def test_campos_serializados(self):
        """Verificar campos serializados"""
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['id', 'codigo_curso', 'descricao', 'nivel_curso']))

    def test_conteudo_campo(self):
        """Verificar conteudo retornado do serializer"""
        data = self.serializer.data
        self.assertEquals(data['id'], self.curso.id)
        self.assertEquals(data['codigo_curso'], self.curso.codigo_curso)
        self.assertEquals(data['descricao'], self.curso.descricao)
        self.assertEquals(data['nivel_curso'], self.curso.nivel_curso)