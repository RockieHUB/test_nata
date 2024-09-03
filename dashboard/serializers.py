from rest_framework import serializers
from .models import Pelatihan

class PelatihanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelatihan
        fields = '__all__'