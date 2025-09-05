from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'arrival_location', 'applicant', 'created_at', 'update_at']
        read_only_fields = ('id', 'created_at', 'update_at') 

    # ---- Validaciones a nivel de campo (field-level) ----
    def validate_brand(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Marca is required.")

    def validate_arrival_location(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Localizacion requerida")
        return value

    def validate_applicant(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Aspirante requerido")
        return value

    def validate(self, attrs):
        if self.instance is None: 
            exists = Vehicle.objects.filter(
                brand__iexact=attrs['brand'],
                arrival_location__iexact=attrs['arrival_location'],
                applicant__iexact=attrs['applicant'],
            ).exists()
            if exists:
                raise serializers.ValidationError({"error": "Un vehiculo similar ya existe"})
        return attrs
