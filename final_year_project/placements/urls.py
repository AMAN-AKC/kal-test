from django.urls import path
from . import views

app_name = 'placements'

urlpatterns = [
    path('', views.add_placement, name='add_placement'),
    path('amazon/', views.amazon_list, name='amazon_list'),
    path('all/', views.all_placements, name='all_placements'),
]
