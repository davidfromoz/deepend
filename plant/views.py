from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Plant, LocalPlant, Tag

def index(request):
    plant_list = LocalPlant.objects.all()
    context = {'plant_list': plant_list}
    return render(request, 'plant/index.html', context)

def detail(request, plant_id):
    plant=LocalPlant.objects.get(id=plant_id)
    context={'plant':plant}
    return render(request, 'plant/detail.html', context)
