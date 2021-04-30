from rest_framework import serializers
from escola.models import Aluno, Matricula
from escola.validators import *

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto']

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ter 11 dígitos"})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        return data

class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['id', 'curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()