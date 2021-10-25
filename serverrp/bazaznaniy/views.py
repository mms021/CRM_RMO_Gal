from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from .models import BazaZnaniy
from .forms import  NewBazaForm
from django.db.models import Q


# Create your views here.
@login_required(login_url='/lg/')
def main_page(request):
    bz = BazaZnaniy.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('rore') == 'dor':
            j = request.POST.get('s') 
            bz = BazaZnaniy.objects.filter(Q(title__icontains= j)| Q(opisan__icontains=j))
            return render(request, 'bazaznaniy/prodject-cate.html', {'bz':bz })
        else:
            form = NewBazaForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
            return redirect('bazaznaniy:main')
    else:
        form = NewBazaForm()
    return render(request, 'bazaznaniy/prodject-bz.html', {'bz':bz , 'form': form })

@login_required(login_url='/lg/')
def page_categoriy(request, pk):
    bz = BazaZnaniy.objects.filter(tip=pk)
    return render(request, 'bazaznaniy/prodject-cate.html', {'bz':bz  })

@login_required(login_url='/lg/')
def page_all(request):
    bz = BazaZnaniy.objects.all()
    return render(request, 'bazaznaniy/prodject-cate.html', {'bz':bz  })



