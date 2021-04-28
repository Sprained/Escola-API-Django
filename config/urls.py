from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from escola.views import AlunosViewset, MatrculasViewset, ListaMatriculasAluno
from curso.views import CursosViewset, ListaMatriculasCurso
from user.views import CreateUserView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Escola API Django",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gabriel.almeida.resende@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

route = routers.DefaultRouter()
route.register('alunos', AlunosViewset, basename='Alunos')
route.register('cursos', CursosViewset, basename='Cursos')
route.register('matriculas', MatrculasViewset, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('user/', CreateUserView.as_view()),
    path('', include(route.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
