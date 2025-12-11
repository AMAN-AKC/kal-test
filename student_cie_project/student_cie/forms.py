from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['usn', 'name', 'subject_code', 'cie_marks']
        widgets = {
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter USN'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'subject_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Code'}),
            'cie_marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter CIE Marks'}),
        }
