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
