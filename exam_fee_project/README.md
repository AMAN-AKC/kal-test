# Exam Fee Project

## Overview

A Django app to manage exam fee entries for students. It stores student fee records in SQLite (Django default) and provides views to add students, list all students, and delete unpaid entries.

## Important files

- `exam_fee/models.py` — model definition for `ExamStudent`.

Example (`exam_fee/models.py`):

```python
from django.db import models

class ExamStudent(models.Model):
    usn = models.CharField(max_length=20, unique=True, verbose_name='USN')
    name = models.CharField(max_length=150, verbose_name='Name')
    semester = models.PositiveSmallIntegerField(verbose_name='Semester')
    fee_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name='Exam Fee Amount')
    fee_paid = models.BooleanField(default=False, verbose_name='Fee Paid')

    def __str__(self):
        return f"{self.usn} - {self.name}"
```

- `exam_fee/forms.py` — `ModelForm` used to create `ExamStudent` entries.

Example (`exam_fee/forms.py`):

```python
from django import forms
from .models import ExamStudent

class ExamStudentForm(forms.ModelForm):
    class Meta:
        model = ExamStudent
        fields = ['usn', 'name', 'semester', 'fee_amount']
        widgets = {
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter USN'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester'}),
            'fee_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fee Amount', 'step': '0.01'}),
        }
```

- `exam_fee/views.py` — add/list/delete views.

Example (`exam_fee/views.py`):

```python
from django.shortcuts import render, redirect
from .forms import ExamStudentForm
from .models import ExamStudent

def add_student(request):
    if request.method == 'POST':
        form = ExamStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # mark fee_paid True if fee_amount > 0
            student.fee_paid = bool(student.fee_amount and student.fee_amount > 0)
            student.save()
            return redirect('exam_fee:list_students')
    else:
        form = ExamStudentForm()
    return render(request, 'exam_fee/add_student.html', {'form': form})

def list_students(request):
    students = ExamStudent.objects.all()
    return render(request, 'exam_fee/list_students.html', {'students': students})

def delete_unpaid(request):
    # delete all students who have not paid (fee_paid == False)
    ExamStudent.objects.filter(fee_paid=False).delete()
    return redirect('exam_fee:list_students')
```

- `exam_fee/urls.py` — app URL patterns (example):

```python
from django.urls import path
from . import views

app_name = 'exam_fee'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('list/', views.list_students, name='list_students'),
    path('delete-unpaid/', views.delete_unpaid, name='delete_unpaid'),
]
```

- Templates:
  - `exam_fee/templates/exam_fee/add_student.html` — form for new entries.
  - `exam_fee/templates/exam_fee/list_students.html` — table of students with `fee_paid` status and a button/link to delete unpaid entries.

## Setup & Run

Assumes a Python virtual environment `myevn` in the workspace root and Django installed there.

On Windows (cmd/PowerShell):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\exam_fee_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Notes

- After creating students via the add form, the view will set `fee_paid=True` when `fee_amount` &gt; 0. If you want manual control for `fee_paid`, add the field to the form and update template accordingly.
- Use the `delete-unpaid/` endpoint (or add a button in the admin/template) to remove all unpaid students.
- Admin: register `ExamStudent` in `exam_fee/admin.py` to manage entries from Django admin.

## Files to review

- `exam_fee/models.py`
- `exam_fee/forms.py`
- `exam_fee/views.py`
- `exam_fee/urls.py`
- `exam_fee/templates/exam_fee/*`
