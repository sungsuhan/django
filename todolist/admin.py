# todolist/admin.py 
from django.contrib import admin

# Register your models here.
# �𵨿��� TodoList ���� ������ 
from .models import TodoList 

# ���� ����Ʈ�� TodoList ���� ��� 
admin.site.register(TodoList)
# Register your models here.
