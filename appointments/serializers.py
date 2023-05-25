from .models import AppointmentsModel
from rest_framework import serializers

class AppointmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = AppointmentsModel
        fields = '__all__'