# HR Project

This Django project `hr_project` contains an `employees` app to add employees and list those with salary > 50,000.

Quick start (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\hr_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000/hr/ (add employee)
High-salary list: http://127.0.0.1:8000/hr/high/
All employees: http://127.0.0.1:8000/hr/all/
