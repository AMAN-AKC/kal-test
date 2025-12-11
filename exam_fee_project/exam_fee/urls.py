from django.urls import path
from . import views

app_name = 'exam_fee'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('list/', views.list_students, name='list_students'),
    path('delete-unpaid/', views.delete_unpaid, name='delete_unpaid'),
]
