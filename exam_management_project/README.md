# Exam Management Project

This Django project `exam_management_project` contains an `exam_app` to add students and list those who secured grade 'O'.

Quick start (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\exam_management_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open:

- Add student: http://127.0.0.1:8000/exam/
- O-grade list: http://127.0.0.1:8000/exam/o-grade/
- All students: http://127.0.0.1:8000/exam/all/
