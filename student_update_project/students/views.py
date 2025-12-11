from django.shortcuts import render, redirect
from .forms import StudentForm, UpdateGradeForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

def update_grade(request):
    updated = []
    if request.method == 'POST':
        form = UpdateGradeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            grade = form.cleaned_data['grade']
            qs = Student.objects.filter(name__iexact=name)
            for s in qs:
                s.grade = grade
                s.save()
            updated = list(qs)
    else:
        form = UpdateGradeForm()
    return render(request, 'students/update_grade.html', {'form': form, 'updated': updated})