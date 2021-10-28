from .models import Cliente
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.

def getUsers():
    router = routers.DefaultRouter()
    router.register(r'clientes', UserViewSet)