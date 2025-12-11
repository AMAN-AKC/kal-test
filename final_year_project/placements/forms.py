from django import forms
from .models import Placement

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['usn', 'name', 'company']
        widgets = {
            'usn': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }
