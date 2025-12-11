from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['usn', 'name', 'subject_code', 'cie_marks']
    search_fields = ['usn', 'name', 'subject_code']
    list_filter = ['cie_marks']
