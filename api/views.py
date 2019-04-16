from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from aporte.models import Aporte
from .serializers import AporteSerializer
# Create your views here.

class AporteDeleteUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Aporte.objects.all()
    serializer_class = AporteSerializer


class AporteView(ListCreateAPIView):
    queryset = Aporte.objects.all()
    serializer_class = AporteSerializer