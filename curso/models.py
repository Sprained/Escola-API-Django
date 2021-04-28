from django.db import models

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255)
    nivel_curso = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'cruso'