# todolist/admin.py 
from django.contrib import admin

# Register your models here.
# ¸ðµ¨¿¡¼­ TodoList ¸ðµ¨À» °¡Á®¿È 
from .models import TodoList 

# ¾îµå¹Î »çÀÌÆ®¿¡ TodoList ¸ðµ¨À» µî·Ï 
admin.site.register(TodoList)
# Register your models here.
