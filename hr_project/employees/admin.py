from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'hired_date', 'job_title', 'salary']
    search_fields = ['name', 'email', 'job_title']
    list_filter = ['job_title']
