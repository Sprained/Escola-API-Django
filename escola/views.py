from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from escola.models import Aluno, Matricula
from escola.serializer import AlunosSerializer, MatriculasSerializer, ListaMatriculasAlunoSerializer

class SetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class AlunosViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    pagination_class = SetPagination
    http_method_names = ['get', 'post', 'put']
    permission_classes = [IsAuthenticated]

class MatrculasViewset(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    permission_classes = [IsAuthenticated]