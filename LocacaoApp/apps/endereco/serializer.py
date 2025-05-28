from .models import EnderecoM
from rest_framework import serializers


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoM
        fields = '__all__'