from django.shortcuts import render
from rest_framework import generics
from .models import App

class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = App
    
    def get_queryset(self):
        return App.objects.all()