from .models import Departments
from rest_framework import serializers

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ["name", "description", "img"]