from django.test import TestCase
from curso.models import Curso

class CursoModelTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo_curso='CTT1', descricao='Curso de teste'
        )
    
    def test_verificar_default(self):
        """Verificar valores funcionamento valores default"""
        self.assertEquals(self.curso.codigo_curso, 'CTT1')
        self.assertEquals(self.curso.descricao, 'Curso de teste')
        self.assertEquals(self.curso.nivel_curso, 'B')