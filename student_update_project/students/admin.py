from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['usn', 'name', 'dept', 'grade']
    search_fields = ['usn', 'name', 'dept']
    list_filter = ['dept', 'grade']
