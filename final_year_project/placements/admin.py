from django.contrib import admin
from .models import Placement


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ['usn', 'name', 'company']
    search_fields = ['usn', 'name', 'company']
