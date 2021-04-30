from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from curso.models import Curso
from escola.models import Matricula
from curso.serializer import CursoSerializer, ListaMatriculasCursoSerializer

class CursosViewset(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [IsAuthenticated]

class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
    permission_classes = [IsAuthenticated]