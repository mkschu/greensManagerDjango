from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Employee,
    Task,
    MowTask,
    TrapTask,
    RecordsTask,
    ShopTask,
    MiscTask,
    WtfTask
)

def curr_time():
    return now()

def index(request):
    context = {
        'curr_time': curr_time(),
    }
    return render(request, 'labor/index.html', context)

def mowTaskIndex(request):
    mowTasks = MowTask.objects.all().order_by('started')

    context = {
        'curr_time': curr_time(),
        'mow_tasks': mowTasks,
    }

    return render(request, 'labor/mow_task_index.html', context)
