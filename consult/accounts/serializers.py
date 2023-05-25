from .models import UserAccount
from rest_framework import serializers

class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["fname", "lname", "email", "password", "img"]