from django.contrib import admin
from escola.models import Aluno, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'rg', 'cpf',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Matricula, Matriculas)