from django.contrib import admin
from django.urls import path, include 
from .views import TodoListAPIView


urlpatterns = [
    path('api/todolist/', TodoListAPIView.as_view(), name="todo-list"), 
    # api/ 다음에 오는 단어에 따라서 호출되는 API 뷰가 달라지게 url pattern을 	  작성할수 있다.
]