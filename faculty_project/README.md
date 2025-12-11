# Faculty Project

This Django project `faculty_project` includes a `faculty` app to record faculty details and list CSE Professors.

Quick start (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\faculty_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open:

- Add faculty: http://127.0.0.1:8000/faculty/
- CSE Professors: http://127.0.0.1:8000/faculty/cse-professors/
- All faculty: http://127.0.0.1:8000/faculty/all/
