from rest_framework import serializers
from curso.models import Curso
from escola.models import Matricula

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='aluno.id')
    nome = serializers.ReadOnlyField(source='aluno.nome')
    cpf = serializers.ReadOnlyField(source='aluno.cpf')
    class Meta:
        model = Matricula
        fields = ['id', 'nome', 'cpf']