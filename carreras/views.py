from rest_framework import viewsets
from .serializers import carreraSerializer
from .models import carrera

#Create your views here.

class carreraView(viewsets.ModelViewSet):

    serializer_class =  carreraSerializer
    queryset = carrera.objects.all()



