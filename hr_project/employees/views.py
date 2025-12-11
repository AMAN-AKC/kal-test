from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:high_salary')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def high_salary(request):
    # salary greater than 50000
    employees = Employee.objects.filter(salary__gt=50000)
    return render(request, 'employees/high_salary.html', {'employees': employees})

def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all_employees.html', {'employees': employees})
