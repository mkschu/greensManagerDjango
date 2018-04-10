from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Maintenance,
    OilChange,
    Repair,
    RepairPart
)

from .forms import (
    OilChangeForm,
    RepairForm,
    RepairRequestForm,
    RepairPartForm
)

import parts.models as Parts
import machines.models as Machines

def curr_time():
    return now()
    
def partsNew(request, repair):
    repair = Maintenance.objects.get(pk=repair)
    form = RepairPartForm(repair=repair)
    
    context = {
        'curr_time': curr_time(),
        'repair': repair,
        'form': form,
    }
    
    return render(request, 'maintenance/parts.html', context)

def partsCreate(request, repair):
    repair = Maintenance.objects.get(pk=repair)
    
    if request.method == 'POST':
        form = RepairPartForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save()
            
            pending_form.save()
            
    if OilChange.objects.filter(pk=repair.pk).exists():
        return redirect('maint:oilchange_detail', pk=repair.pk)
    elif Repair.objects.filter(pk=repair.pk).exists():
        return redirect('maint:repair_detail', pk=repair.pk)

def oilchangeIndex(request):
    oilchanges = OilChange.objects.all().order_by('-updated_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'oilchanges': oilchanges,
    }
    
    return render(request, 'maintenance/oil_index.html', context)

def oilchangeNew(request):
    form = OilChangeForm()
    part_form = RepairPartForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
        'part_form': part_form,
    }
    
    return render(request, 'maintenance/oil_new.html', context)

def oilchangeCreate(request):
    if request.method == 'POST':
        form = OilChangeForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.oil_cost = pending_form.oil.price_per_unit * \
                pending_form.oil_qty
            
            pending_form.total_cost = pending_form.oil_cost
            
            pending_form.save()
            form.save_m2m()
            
            for p in pending_form.parts_used.all():
                pending_form.total_cost += p.price
                part = Parts.Part.objects.get(pk=p.pk)
                part.in_stock -= 1
                part.save()
                
            pending_form.save()
            
    return redirect('maint:parts_new', repair=pending_form.pk)
                
def oilchangeDetail(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
    }
    
    return render(request, 'maintenance/oil_detail.html', context)

def oilchangeEdit(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    form = OilChangeForm(instance=oilchange)
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
        'form': form,
    }
    
    return render(request, 'maintenance/oil_edit.html', context)

def oilchangeUpdate(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = OilChangeForm(request.POST, instance=oilchange)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.oil_cost = pending_form.oil.price_per_unit* \
                pending_form.oil_qty
            
            pending_form.total_cost = pending_form.oil_cost
            
            pending_form.save()
            form.save_m2m()
            
            for p in pending_form.parts_used.all():
                pending_form.total_cost += p.price
                
            pending_form.save()
            
    return redirect('maint:oilchange_detail', pk=oilchange.pk)

def repairIndex(request):
    repairs = Repair.objects.all().order_by('-updated_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'repairs': repairs,
    }
    
    return render(request, 'maintenance/repair_index.html', context)

def repairNew(request):
    form = RepairForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'maintenance/repair_new.html', context)

def repairNeeded(request):
    form = RepairRequestForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'maintenance/repair_needed.html', context)

def repairRequest(request):
    if request.method == 'POST':
        form = RepairRequestForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.total_cost = 0
            pending_form.save()
            form.save_m2m()
            
            machine = Machines.Machine.objects.get(
                    pk=pending_form.machine.pk)
            machine.in_commission = False
            machine.save()
            
    return redirect('maint:repair_detail', pk=pending_form.pk)

def repairCreate(request):
    if request.method == 'POST':
        form = RepairForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.total_cost = 0
            
            pending_form.save()
            form.save_m2m()
            
            for p in pending_form.parts_used.all():
                pending_form.total_cost += p.price
                part = Parts.Part.objects.get(pk=p.pk)
                part.in_stock -= 1
                part.save()
            
            if pending_form.date_fixed == None:
                machine = Machines.Machine.objects.get(
                        pk=pending_form.machine.pk)
                machine.in_commission = False
                machine.save()
                
        pending_form.save()
        
    return redirect('maint:repair_detail', pk=pending_form.pk)

def repairDetail(request, pk):
    repair = Repair.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'repair': repair,
    }
    
    return render(request, 'maintenance/repair_detail.html', context)

def repairEdit(request, pk):
    repair = Repair.objects.get(pk=pk)
    form = RepairForm(instance=repair)
    
    context = {
        'curr_time': curr_time(),
        'repair': repair,
        'form': form,
    }
    
    return render(request, 'maintenance/repair_edit.html', context)

def repairUpdate(request, pk):
    repair = Repair.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            
            for p in pending_form.parts_used.all():
                pending_form.total_cost += p.price
                part = Parts.Part.objects.get(pk=p.pk)
                part.in_stock -= 1
                part.save()
            
            if pending_form.date_fixed == None:
                machine = Machines.Machine.objects.get(
                        pk=pending_form.machine.pk)
                machine.in_commission = False
                machine.save()
            
            else:
                machine = Machines.Machine.objects.get(
                    pk=pending_form.machine.pk)
                machine.in_commission = True
                machine.save()
                
            pending_form.save()
                
    return redirect('maint:repair_detail', pk=pending_form.pk)
            
