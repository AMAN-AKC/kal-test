from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.add_faculty, name='add_faculty'),
    path('cse-professors/', views.cse_professors, name='cse_professors'),
    path('all/', views.all_faculty, name='all_faculty'),
]
