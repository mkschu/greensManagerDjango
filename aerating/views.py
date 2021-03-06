from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Aerating,
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating,
    QuadraTining,
    DeepTine,
)

from .forms import (
    AeratingForm,
    GreensAeratingForm,
    TeeAeratingForm,
    FairwayAeratingForm,
    RoughAeratingForm,
    QuadraTiningForm,
    DeepTineForm,
)

def curr_time():
    return now()

def qtIndex(request):
    aeratings = QuadraTining.objects.all().order_by('-aerate_date')[:20]

    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }

    return render(request, 'aerating/qt_index.html', context)

def qtNew(request):
    form = QuadraTiningForm()

    context = {
        'curr_time': curr_time(),
        'form': form,
    }

    return render(request, 'aerating/qt_new.html', context)

def qtCreate(request):
    if request.method == 'POST':
        form = QuadraTiningForm(data=request.POST)

        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()

    return redirect('aerate:greens_detail', pk=pending_form.pk)

def dtIndex(request):
    aeratings = DeepTine.objects.all().order_by('-updated_at')[:20]

    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }

    return render(request, 'aerating/dt_index.html', context)

def dtNew(request):
    form = DeepTineForm()

    context = {
        'curr_time': curr_time(),
        'form': form,
    }

    return render(request, 'aerating/dt_new.html', context)

def dtCreate(request):
    if request.method == 'POST':
        form = DeepTineForm(data=request.POST)

        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)

            pending_form.save()
            form.save_m2m()

    return redirect('aerate:greens_detail', pk=pending_form.pk)


def index(request):
    aeratings = Aerating.objects.all().order_by('-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/index.html', context)

def greensIndex(request):
    aeratings = GreensAerating.objects.all().order_by(
        '-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/greens_index.html', context)
    
def greensNew(request):
    form = GreensAeratingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'aerating/greens_new.html', context)

def greensCreate(request):
    if request.method == 'POST':
        form = GreensAeratingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:greens_detail', pk=pending_form.pk)

def greensDetail(request, pk):
    if GreensAerating.objects.filter(pk=pk).exists():
        aerating = GreensAerating.objects.get(pk=pk)
    elif QuadraTining.objects.filter(pk=pk).exists():
        aerating = QuadraTining.objects.get(pk=pk)
    elif DeepTine.objects.filter(pk=pk).exists():
        aerating = DeepTine.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
    }
    
    return render(request, 'aerating/greens_detail.html', context)

def greensEdit(request, pk):
    if GreensAerating.objects.filter(pk=pk).exists():
        aerating = GreensAerating.objects.get(pk=pk)
        form = GreensAeratingForm(instance=aerating)
    elif QuadraTining.objects.filter(pk=pk).exists():
        aerating = QuadraTining.objects.get(pk=pk)
        form = QuadraTiningForm(instance=aerating)
    elif DeepTine.objects.filter(pk=pk).exists():
        aerating = DeepTine.objects.get(pk=pk)
        form = DeepTineForm(instance=aerating)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
        'form': form,
    }
    
    return render(request, 'aerating/greens_edit.html', context)

def greensUpdate(request, pk):
    if GreensAerating.objects.filter(pk=pk).exists():
        aerating = GreensAerating.objects.get(pk=pk)
    elif QuadraTining.objects.filter(pk=pk).exists():
        aerating = QuadraTining.objects.get(pk=pk)
    elif DeepTine.objects.filter(pk=pk).exists():
        aerating = DeepTine.objects.get(pk=pk)
    
    if request.method == 'POST':
        if GreensAerating.objects.filter(pk=pk).exists():
            form = GreensAeratingForm(request.POST, instance=aerating)
        elif QuadraTining.objects.filter(pk=pk).exists():
            form = QuadraTiningForm(request.POST, instance=aerating)
        elif DeepTine.objects.filter(pk=pk).exists():
            form = DeepTineForm(request.POST, instance=aerating)

        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:greens_detail', pk=aerating.pk)

def teesIndex(request):
    aeratings = TeeAerating.objects.all().order_by(
        '-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/tees_index.html', context)

def teesNew(request):
    form = TeeAeratingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'aerating/tees_new.html', context)

def teesCreate(request):
    if request.method == 'POST':
        form = TeeAeratingForm(data=request.POST)
        
        if form.is_valid() and request.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()

def teesDetail(request, pk):
    aerating = TeeAerating.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
    }
    
    return render(request, 'aerating/tees_detail.html', context)

def teesEdit(request, pk):
    aerating = TeeAerating.objects.get(pk=pk)
    form = TeeAeratingForm(instance=aerating)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
        'form': form,
    }
    
    return render(request, 'aerating/tees_edit.html', context)

def teesUpdate(request, pk):
    aerating = TeeAerating.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TeeAeratingForm(request.POST, instance=aerating)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:tees_detail', pk=aerating.pk)

def fairwaysIndex(request):
    aeratings = FairwayAerating.objects.all().order_by(
        '-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/fairways_index.html', context)

def fairwaysNew(request):
    form = FairwayAeratingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'aerating/fairways_new.html', context)

def fairwaysCreate(request):
    if request.method == 'POST':
        form = FairwayAeratingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:fairways_detail', pk=pending_form.pk)

def fairwaysDetail(request, pk):
    aerating = FairwayAerating.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
    }
    
    return render(request, 'aerating/fairways_detail.html', context)

def fairwaysEdit(request, pk):
    aerating = FairwayAerating.objects.get(pk=pk)
    form = FairwayAeratingForm(instance=aerating)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
        'form': form,
    }
    
    return render(request, 'aerating/fairways_edit.html', context)

def fairwaysUpdate(request, pk):
    aerating = FairwayAerating.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FairwayAeratingForm(request.POST, instance=aerating)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:fairways_detail', pk=aerating.pk)

def roughsIndex(request):
    aeratings = RoughAerating.objects.all().order_by(
        '-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/roughs_index.html', context)

def roughsNew(request):
    form = RoughAeratingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'aerating/roughs_new.html', context)

def roughsCreate(request):
    if request.method == 'POST':
        form = RoughAeratingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
    
    return redirect('aerate:roughs_new', pk=pending_form.pk)

def roughsDetail(request, pk):
    aerating = RoughAerating.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
    }
    
    return render(request, 'aerating/roughs_detail.html', context)

def roughsEdit(request, pk):
    aerating = RoughAerating.objects.get(pk=pk)
    form = RoughAeratingForm(instance=aerating)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
        'form': form,
    }
    
    return render(request, 'aerating/roughs_edit.html', context)

def roughsUpdate(request, pk):
    aerating = RoughAerating.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RoughAeratingForm(request.POST, instance=aerating)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:roughs_detail', pk=aerating.pk)
