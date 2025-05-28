from django.shortcuts import render
from .models import EnderecoM
from .serializer import EnderecoSerializer
from rest_framework import viewsets

class EnderecoMViewSet(viewsets.ModelViewSet):
    queryset = EnderecoM.objects.all()
    serializer_class = EnderecoSerializer
