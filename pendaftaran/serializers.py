from rest_framework import serializers
from .models import Akun

class AkunItemSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Akun
        fields = ['fullname', 'email', 'phoneNumber', 'password', 'confirmPassword', 'userRole']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match.")
        data.pop("confirmPassword")
        return data