Biodata Project
===============

Overview
--------
A minimal Django app that displays a biodata form and shows the submitted data on a results page. This app does not use the database; it uses a plain `Form` and renders the cleaned data.

Important files
---------------
- `biodata/forms.py` — defines the form fields shown to the user.

Example (`biodata/forms.py`):

```python
from django import forms

class BiodataForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your address','rows':3}))
```

- `biodata/views.py` — handles form display and submission (renders a display template with cleaned data).

Example (`biodata/views.py`):

```python
from django.shortcuts import render
from .forms import BiodataForm

def biodata_form(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'biodata/display.html', {'data': data})
    else:
        form = BiodataForm()
    return render(request, 'biodata/form.html', {'form': form})
```

- `biodata/templates/biodata/form.html` — form template (simple HTML form posting to the same view).
- `biodata/templates/biodata/display.html` — display template that shows submitted fields.
- `biodata/urls.py` — app URL configuration; typically includes a path to `biodata_form` view.
- Project-level `urls.py` (in `biodata_project/`) — must include the `biodata` app's URLs, for example:

```python
from django.urls import path, include

urlpatterns = [
    path('biodata/', include('biodata.urls')),
]
```

Setup & Run
-----------
Assumes you have a Python virtual environment named `myevn` in the workspace root and Django installed there. No database migrations are required for this app.

On Windows (PowerShell or cmd):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\biodata_project"
..\myevn\Scripts\activate
pip install django
python manage.py runserver
```

Open in a browser:

- If the app is mounted at `biodata/`: http://127.0.0.1:8000/biodata/
- If the app was wired to root (`''`) in project `urls.py`: http://127.0.0.1:8000/

Notes
-----
- This app is intentionally DB-free; it's useful for front-end form demos.
- If you want to persist submissions, convert `BiodataForm` into a `ModelForm` and add a `Biodata` model in `models.py`, then run `makemigrations` and `migrate`.

Files to review
---------------
- `biodata/forms.py` — form fields and widgets
- `biodata/views.py` — submission handling
- `biodata/templates/biodata/form.html` — HTML form
- `biodata/templates/biodata/display.html` — result display
- `biodata/urls.py` and `biodata_project/urls.py` — routing

