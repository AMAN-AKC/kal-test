from django.contrib import admin
from .models import ExamStudent

# Register your models here.

@admin.register(ExamStudent)
class ExamStudentAdmin(admin.ModelAdmin):
	list_display = ['usn', 'name', 'semester', 'fee_amount', 'fee_paid']
	search_fields = ['usn', 'name']
	list_filter = ['semester', 'fee_paid']
