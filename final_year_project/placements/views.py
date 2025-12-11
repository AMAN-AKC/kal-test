from django.shortcuts import render, redirect
from .forms import PlacementForm
from .models import Placement

def add_placement(request):
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('placements:amazon_list')
    else:
        form = PlacementForm()
    return render(request, 'placements/add_placement.html', {'form': form})

def amazon_list(request):
    students = Placement.objects.filter(company__icontains='amazon')
    return render(request, 'placements/amazon_list.html', {'students': students})

def all_placements(request):
    students = Placement.objects.all()
    return render(request, 'placements/all_placements.html', {'students': students})
