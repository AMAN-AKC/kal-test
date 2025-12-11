from django.urls import path
from . import views

app_name = 'exam_app'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('o-grade/', views.ograde_students, name='ograde'),
    path('all/', views.all_students, name='all_students'),
]
