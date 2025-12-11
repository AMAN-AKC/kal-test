from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_app:ograde')
    else:
        form = StudentForm()
    return render(request, 'exam_app/add_student.html', {'form': form})

def ograde_students(request):
    students = Student.objects.filter(grade='O')
    return render(request, 'exam_app/ograde_students.html', {'students': students})

def all_students(request):
    students = Student.objects.all()
    return render(request, 'exam_app/all_students.html', {'students': students})
