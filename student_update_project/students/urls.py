from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('list/', views.list_students, name='list_students'),
    path('update-grade/', views.update_grade, name='update_grade'),
]
