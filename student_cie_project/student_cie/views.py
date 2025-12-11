from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_cie:display_low_cie')
    else:
        form = StudentForm()
    
    return render(request, 'student_cie/add_student.html', {'form': form})

def display_low_cie(request):
    students = Student.objects.filter(cie_marks__lt=20)
    return render(request, 'student_cie/display_students.html', {'students': students})

def all_students(request):
    students = Student.objects.all()
    return render(request, 'student_cie/all_students.html', {'students': students})
