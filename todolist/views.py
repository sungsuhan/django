from django.shortcuts import render

from .models import TodoList 
from rest_framework import generics 
# serializers.py 파일에서 정의한 TodoSerializer를 가져옴
from .serializers import TodoSerializer  


# Create your views here.

class TodoListAPIView(generics.ListAPIView):
    queryset = TodoList.objects.all() 
    serializer_class = TodoSerializer

# Create your views here.
