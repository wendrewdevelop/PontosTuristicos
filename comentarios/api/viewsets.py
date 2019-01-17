from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer

class ComentarioViewset(ModelViewSet):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.all()