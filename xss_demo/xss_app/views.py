from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
import re

def vulnerable_xss(request):
    """Demonstrates XSS vulnerability - UNSAFE"""
    name = ""
    if request.method == 'POST':
        name = request.POST.get('name', '')
    
    context = {
        'name': name,
        'vulnerability_type': 'Vulnerable (Unsafe)'
    }
    return render(request, 'xss_app/vulnerable.html', context)
