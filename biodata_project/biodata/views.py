from django.shortcuts import render
from .forms import BiodataForm

# Create your views here.

def biodata_form(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            # Get cleaned data and pass to display template
            data = form.cleaned_data
            return render(request, 'biodata/display.html', {'data': data})
    else:
        form = BiodataForm()
    
    return render(request, 'biodata/form.html', {'form': form})
