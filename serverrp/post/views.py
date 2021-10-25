from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from .models import NomerForPismo
# Create your views here.
from datetime import datetime , timedelta 
from .forms import FileForm , PismoForm

@login_required(login_url='/lg/')
def post_page(request):
    nom = NomerForPismo.objects.all()
    if request.method == 'POST':
        if request.POST.get('tip') == "old":
            nou = NomerForPismo()
            nou.title = request.POST.get('title')
            nou.komy = request.POST.get('komy')
            nou.ochem = request.POST.get('ochem')
            nou.otvetstven = request.user.first_name
            nou.data = request.POST.get('data')
            nou.pernom = request.POST.get('pernom')

            try:
                j = NomerForPismo.objects.filter(title=request.POST.get('title')).filter(nomer=request.POST.get('pernom')).first() 
                if j.pernom == None:
                    nou.nomer = 1
                else:
                    j = NomerForPismo.objects.filter(title=request.POST.get('title')).filter(pernom=request.POST.get('pernom')).first() 
                    nou.nomer =int(j.nomer)+1
            except :
                nou.nomer = 1

            nou.save()
        else:
            nou = NomerForPismo()
            nou.title = request.POST.get('title')
            nou.komy = request.POST.get('komy')
            nou.ochem = request.POST.get('ochem')
            nou.otvetstven = request.user.first_name
            nou.data = request.POST.get('data')
            try:
                j = NomerForPismo.objects.filter(title=request.POST.get('title')).filter(pernom=None).first() 
                nou.nomer = int(j.nomer) + 1
            except :
                nou.nomer = 1
            nou.save()   
        

        nom = NomerForPismo.objects.all()
        nomle = NomerForPismo.objects.all().first()
        return render(request, 'post/prodject-post-all.html', {'nom':nom ,"nomle":nomle ,"idollcontacts":'showme' })
    return render(request, 'post/prodject-post-all.html', {'nom':nom})

@login_required(login_url='/lg/')
def post_page_name(request, pk):
    nom = NomerForPismo.objects.filter(otvetstven= pk)
    return render(request, 'post/prodject-post-all-name.html', {'nom':nom , "pk":pk})

@login_required(login_url='/lg/')
def post_page_gen(request):


    from docxtpl  import DocxTemplate
    if request.method == 'POST':
        #pk = 'jj'
        now = str(datetime.today())
        fio = request.POST.get('fio')
        dd = fio.split(' ')
        now = now.split('-')
        
        doc12 = DocxTemplate("media/PesmoGalpro.docx") 
        context = { 'nom': '__' , 'fio': str(dd[1] +' ' + dd[2]), 'fiosok':  str(dd[1][0] +'. ' + dd[2][0]+ '. '+ dd[0] ), 'komy': request.POST.get('komy'), 'datatud' : str(now[2][0:2]+'.'+now[1]+'.'+now[0]),
                'trxt': request.POST.get('trxt')  , 'fioifpl': str(request.user.first_name) , 'mailisp' :str(request.user.email) 
                }
        doc12.render(context)
        doc12.save("media/Pismo.docx")
        return redirect("/p/%s/" % ('Pismo.docx'))

    return render(request, 'post/prodject-post.html')

@login_required(login_url='/lg/')
def post_page_generate(request,pk):

    return render(request, 'post/prodject-douland.html',{'ind':pk})
    
@login_required(login_url='/lg/')
def post_dowlend(request,pk):
    nom = NomerForPismo.objects.get(id= pk)
    if request.method == 'POST':
        form = PismoForm(request.POST, request.FILES , instance=nom)
        if form.is_valid():
            form.save()
            return redirect("/p/")
    else: 
        form = PismoForm(instance=nom)
    return render(request, 'post/prodject-post-dowlend.html', {'nom':nom , 'form':form })





