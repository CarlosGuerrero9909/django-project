from rest_framework import serializers
from .models import carrera
from materias.models import materia
from materias.serializers import materiaSerializer 

class carreraSerializer (serializers.ModelSerializer):
    materias = materiaSerializer(many=True)

    class Meta:
        model = carrera
        fields = (
            'codigo', 'nombre', "materias"
        )

    def create(self, validated_data):
        _carrera = carrera(nombre=validated_data.get("nombre"))
        _carrera.save()

        materias=validated_data.get('materias')

        for _materia in materias:
            materia.objects.create(carrera=_carrera, **_materia)

        return validated_data
