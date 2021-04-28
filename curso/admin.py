from django.contrib import admin
from curso.models import Curso

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel_curso')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Curso, Cursos)