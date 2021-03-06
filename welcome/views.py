from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib.auth import authenticate, login

from courses import models as Courses
from fertilizing import models as Fert
from irrigation import models as Irrig
from machines import models as Machines
from parts import models as Parts
from turfs import models as Turfs
from mowing import models as Mow
from rolling import models as Roll
from notes import models as Notes

from notes import forms as NoteF

from .calcMowDirections import *
from .forms import *

def curr_time():
    return now()

def login_page(request):

    if request.method == 'GET':

        form = LoginForm()
        context = {
            'form': form,
            'curr_time': curr_time(),
        }

        return render(request, 'welcome/login.html', context)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username, 
                            password=password)

        if user is not None:
            login(request, user)

            return redirect('welcome:index')

        else:
            return redirect('welcome:login')


def index(request):

    if request.user.is_authenticated() == False:
        return redirect('welcome:login')

    course_list = Courses.Course.objects.all()
    hole_list = Courses.Hole.objects.all()
    box_probs = Irrig.SatelliteBox.objects.filter(problem=True)
    sprinkler_probs = \
        Irrig.SprinklerHead.objects.filter(problem=True)
    drain_probs = \
        Irrig.Drain.objects.filter(problem=True)
    oos_parts = \
        Parts.Part.objects.filter(in_stock=0) \
            .order_by('-updated_at')[:5]
    greens_mowing = \
        Mow.GreensMowing.objects.all().order_by('-mow_date')[:5]
    tee_mowing = \
        Mow.TeeMowing.objects.all().order_by('-mow_date')[:5]
    greens_rolling = \
        Roll.GreensRolling.objects.all().order_by('-roll_date')[:5]
    recent_fert = \
        Fert.Fertilizing.objects.all().order_by('-fert_date')[:5]
    greens_fert = \
        Fert.GreensFert.objects.all().order_by('-fert_date')[:5]
    tees_fert = \
        Fert.TeeFert.objects.all().order_by('-fert_date')[:5]
    ooc_machines = \
        Machines.Machine.objects.filter(in_commission=False) \
            .order_by('-updated_at')[:5]


    try:
        daily_notes = \
            Notes.DailyNote.objects.get(valid_date=curr_time)

    except Exception:
        daily_notes = \
        Notes.DailyNote.objects.all().order_by('-valid_date').first()

    daily_form = NoteF.DailyNoteEdit(instance=daily_notes)

    try:
        weekly_notes = \
            Notes.WeeklyNote.objects.filter(end_date__gte=curr_time).order_by(
                'start_date').first()
    except Exception:
        weekly_notes = \
            Notes.WeeklyNote.objects.all().order_by('-end_date').first()

    weekly_form = NoteF.WeeklyNoteEdit(instance=weekly_notes)

    context = {
        'curr_time': curr_time,
        'course_list': course_list,
        'hole_list': hole_list,
        'box_probs': box_probs,
        'sprinkler_probs': sprinkler_probs,
        'drain_probs': drain_probs,
        'oos_parts': oos_parts,
        'greens_mowing': greens_mowing,
        'tee_mowing': tee_mowing,
        'greens_roll': greens_rolling,
        'recent_fert': recent_fert,
        'greens_fert': greens_fert,
        'tees_fert': tees_fert,
        'ooc_machines': ooc_machines,
        'daily_notes': daily_notes,
        'daily_form': daily_form,
        'weekly_notes': weekly_notes,
        'weekly_form': weekly_form,
    }

    return render(request, 'welcome/index.html', context)

def daily(request):
    curr_time = now()

    context = {
        'curr_time': curr_time,
    }
    return render(request, 'welcome/daily.html', context)

