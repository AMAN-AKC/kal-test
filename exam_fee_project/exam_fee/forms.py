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
