# Student Update Project

This Django project `student_update_project` contains a `students` app to add students and update grades by student name.

Quick start (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\student_update_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open:

- Add student: http://127.0.0.1:8000/students/
- List students: http://127.0.0.1:8000/students/list/
- Update grade by name: http://127.0.0.1:8000/students/update-grade/
