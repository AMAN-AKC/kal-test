from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_id', 'title', 'name', 'branch']
    search_fields = ['faculty_id', 'name', 'branch']
    list_filter = ['branch', 'title']
