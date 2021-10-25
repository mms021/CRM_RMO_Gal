from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from projects.models import Projects , Itap
from resurses.models import  Cotrudniri , Otdel
from .models import OtMonf , PlanForMyWok


# Create your views here.
# ПЛАН ПРОЕКТОВ 
@login_required(login_url='/lg/')
def my_prodjects_plan(request):
    prog = Projects.objects.filter(rpproecta=request.user.first_name ).exclude(activedog = "Завершен").order_by('-activedog') #request.user.first_name  "Максим Пех"
    cont = Cotrudniri.objects.exclude(statusof='Уволен').filter(tip='sotrudnic').filter(projects__in=prog).distinct()
    otc = OtMonf.objects.all()  #[-3:-1]
    otd = Otdel.objects.all()
    if request.method == 'POST':
        otc = OtMonf.objects.get(id=request.POST.get('idofot')) 
        o =0
        dpds = request.POST.getlist('checid')
        for i in request.POST.getlist('proz'):    
            if i != '-':
                try:
                    p =  PlanForMyWok.objects.filter(projects__id=dpds[o].split('?')[0]).filter(cotrud__index=dpds[o].split('?')[1]).filter(otch=otc).get()
                    p.title = i
                    p.save()
                except:
                    p = PlanForMyWok()
                    p.title = i
                    p.projects = Projects.objects.get(id= dpds[o].split('?')[0])
                    p.cotrud = Cotrudniri.objects.get(index=dpds[o].split('?')[1])
                    p.otch = otc
                    p.save()
            o +=1
        return redirect("/plan/plan" ) 
    return render(request, 'resorsplaning/prodject-plan.html',{'prog':prog , 'cont':cont,'otc':otc ,'otd':otd})


@login_required(login_url='/lg/')
def otdel_prodjects_plan(request, pk):
    cont = Cotrudniri.objects.exclude(statusof='Уволен').filter(tip='sotrudnic').filter(ondel__id=pk).distinct()
    f = []
    for i in cont:
        for g in i.projects.all():
            f.append(g.id)
    
    prog = Projects.objects.exclude(activedog = "Завершен").filter(id__in =f).order_by('-activedog') #request.user.first_name  "Максим Пех"
    otc = OtMonf.objects.all()  #[-3:-1]
    otd = Otdel.objects.all()
    if request.method == 'POST':
        otc = OtMonf.objects.get(id=request.POST.get('idofot')) 
        o =0
        dpds = request.POST.getlist('checid')
        for i in request.POST.getlist('proz'):    
            if i != '-':
                try:
                    p =  PlanForMyWok.objects.filter(projects__id=dpds[o].split('?')[0]).filter(cotrud__index=dpds[o].split('?')[1]).filter(otch=otc).get()
                    p.title = i
                    p.save()
                except:
                    p = PlanForMyWok()
                    p.title = i
                    p.projects = Projects.objects.get(id= dpds[o].split('?')[0])
                    p.cotrud = Cotrudniri.objects.get(index=dpds[o].split('?')[1])
                    p.otch = otc
                    p.save()
            o +=1
        return redirect(f"/plan/plan/{pk}" ) 

    return render(request, 'resorsplaning/prodject-plan-otd.html',{'prog':prog , 'cont':cont,'otc':otc ,'otd':otd})













