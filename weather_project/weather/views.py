from django.shortcuts import render
from .forms import CityForm
import requests

API_KEY = '5adbed3462abeb36442b53e62be8a29b'

def index(request):
    weather = None
    error = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city'].strip()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                resp = requests.get(url, timeout=10)
                data = resp.json()
                if resp.status_code == 200 and data.get('cod') == 200:
                    weather = {
                        'city': data.get('name'),
                        'temp': data.get('main', {}).get('temp'),
                        'description': data.get('weather', [{}])[0].get('description', '').title(),
                    }
                else:
                    # OpenWeather returns cod and message on error
                    error = data.get('message', 'City not found')
            except requests.RequestException:
                error = 'Error contacting weather service.'
    else:
        form = CityForm()
    return render(request, 'weather/index.html', {'form': form, 'weather': weather, 'error': error})
