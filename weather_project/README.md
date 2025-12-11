# Weather Project

A minimal Django app that fetches live weather from OpenWeatherMap API (no database used).

API key used: 5adbed3462abeb36442b53e62be8a29b

Run (Windows, using your `myevn` venv):

```powershell
cd "c:\Users\amanc\Desktop\CODE\kal test\weather_project"
..\myevn\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Open: http://127.0.0.1:8000/ and enter a city name.

Notes:

- Invalid city names will show an error message returned by the API.
- No database is required for this app.
