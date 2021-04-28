from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Matricula
from escola.serializer import AlunosSerializer, MatriculasSerializer, ListaMatriculasAlunoSerializer

class AlunosViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    permission_classes = [IsAuthenticated]

class MatrculasViewset(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    permission_classes = [IsAuthenticated]