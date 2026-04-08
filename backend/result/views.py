from django.shortcuts import render
from rest_framework import generics
from .models import Result as ResultModel
from .models import MarkSheet as MarkSheetModel
from .serializers import ResultSerializer, MarkSheetSerializer

class ResultView(generics.ListCreateAPIView):
    queryset=ResultModel.objects.all()
    serializer_class=ResultSerializer

class MarkSheetView(generics.ListCreateAPIView):
    queryset=MarkSheetModel.objects.all()
    serializer_class=MarkSheetSerializer
