from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer

class ComentarioViewset(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer