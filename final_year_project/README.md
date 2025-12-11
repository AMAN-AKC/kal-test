Final Year Placements Project
=============================

This Django project `final_year_project` contains a `placements` app to record final-year placements and list students placed at Amazon.

Quick start (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\final_year_project"
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open:
- Add placement: http://127.0.0.1:8000/placements/
- Amazon placements: http://127.0.0.1:8000/placements/amazon/
- All placements: http://127.0.0.1:8000/placements/all/
