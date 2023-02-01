from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout

from .models import *
from .forms import *



def measurements(request):
    if request.user.is_authenticated:
        last = Measurements.objects.order_by('-Date')[0]  # for last user's value

    if request.method == 'POST':
        form = AddMeasurements(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('measurements')
    else:
        form = AddMeasurements()
    if request.user.is_authenticated:
        context = {
        'title': 'Add measurements',
        'measurements': Measurements.objects.filter(user=request.user),
        'form': form,
        'last':  last, # for last user's value
        }
        return render(request, 'measurements/measurements.html', context=context)
    else:
        context = {
        'title': 'Add measurements',
        }
        return render(request, 'measurements/measurements.html', context=context)


def meas_add(request):
    last = Measurements.objects.order_by('-Date')[0]  # for last user's value

    if request.method == 'POST':
        form = AddMeasurements(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('measurements')
    else:
        form = AddMeasurements()
    if request.user.is_authenticated:
        context = {
        'title': 'Add measurements',
        'measurements': Measurements.objects.filter(user=request.user),
        'form': form,
        'last':  last, # for last user's value
        }
        return render(request, 'measurements/meas_add.html', context=context)
    else:
        context = {
        'title': 'Add measurements',
        }
        return render(request, 'measurements/meas_add.html', context=context)


def comparison(request, comp_pk):
    if Measurements.objects.filter(user=request.user).order_by('-Date')[0]:
        last = Measurements.objects.filter(user=request.user).order_by('-Date')[0]   # for last user's value
    meas = get_object_or_404(Measurements, pk=comp_pk)
    dif_Shoulders = int(last.Shoulders) - int(meas.Shoulders)
    dif_Chest = int(last.Chest) - int(meas.Chest)
    dif_Waist = int(last.Waist) - int(meas.Waist)
    dif_Buttocks = int(last.Buttocks) - int(meas.Buttocks)
    dif_Hips = int(last.Hips) - int(meas.Hips)
    dif_Weight = round(float(last.Weight) - float(meas.Weight), 2)
    context = {
        'title': 'Comparison measurements',
        'comp': comp_pk.title(),
        'last': last,  # for last user's value
        'meas': meas,
        'measurements': Measurements.objects.filter(user=request.user),
        'dif_Shoulders': dif_Shoulders,
        'dif_Chest': dif_Chest,
        'dif_Waist': dif_Waist,
        'dif_Buttocks': dif_Buttocks,
        'dif_Hips': dif_Hips,
        'dif_Weight': dif_Weight,
    }
    return render(request, 'measurements/comparison.html', context=context)



