from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['usn', 'name', 'semester', 'subject_code', 'grade']
    search_fields = ['usn', 'name', 'subject_code']
    list_filter = ['grade', 'semester']
