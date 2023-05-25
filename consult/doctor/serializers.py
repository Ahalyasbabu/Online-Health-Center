from .models import Doctor
from rest_framework import serializers

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'