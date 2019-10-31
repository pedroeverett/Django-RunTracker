from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from decimal import Decimal
import copy

from .models import Runtracker
from .forms import RuntrackerForm

def index(request):
    run_list = Runtracker.objects.order_by('id')
    newRunList = Runtracker.objects.all()

    for run in newRunList:
        def calc_calories():
            hours = float(run.time) / 60
            km = float(run.distance) / 1000
            kph = km / hours
            # massKg value is average body mass for person with 180cm and 75kg, as calculated in https://www.diabetes.ca/en-CA/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
            masskg = 23.1
            vo2 = 2.209 + 3.1633 * kph
            kCalMin = 4.86 * masskg * vo2 / 1000
            return kCalMin

        run.calories = calc_calories()
        run.save()

    context = {'run_list' : run_list}

    return render(request, 'runtracker/index.html', context)

def newForm(request):
    form = RuntrackerForm()

    context = {'form' : form}

    return render(request, 'runtracker/form.html', context)


@require_POST
def addRun(request):
    form = RuntrackerForm(request.POST)

    if form.is_valid():
        new_run = Runtracker(date=request.POST['date'], distance=request.POST['distance'], time=request.POST['time'], calories=0)
        new_run.save()

    return redirect('index')