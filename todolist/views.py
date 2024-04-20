from django.shortcuts import render

from .models import TodoList 
from rest_framework import generics 
# serializers.py ���Ͽ��� ������ TodoSerializer�� ������
from .serializers import TodoSerializer  


# Create your views here.

class TodoListAPIView(generics.ListAPIView):
    queryset = TodoList.objects.all() 
    serializer_class = TodoSerializer

# Create your views here.
