from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty:cse_professors')
    else:
        form = FacultyForm()
    return render(request, 'faculty/add_faculty.html', {'form': form})

def cse_professors(request):
    # filter branch CSE and title Professor (case-insensitive)
    facs = Faculty.objects.filter(branch__iexact='CSE', title__iexact='Professor')
    return render(request, 'faculty/cse_professors.html', {'faculties': facs})

def all_faculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/all_faculty.html', {'faculties': faculties})
