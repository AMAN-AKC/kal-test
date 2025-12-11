from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.add_employee, name='add_employee'),
    path('high/', views.high_salary, name='high_salary'),
    path('all/', views.all_employees, name='all_employees'),
]
