from django.urls import path
from . import views

app_name = 'student_cie'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('low-cie/', views.display_low_cie, name='display_low_cie'),
    path('all-students/', views.all_students, name='all_students'),
]
