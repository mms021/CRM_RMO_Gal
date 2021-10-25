
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Projects , Itap , Komanda , Zadania , Dopsog , Zadachirp , Risk , Problems , Mani , Documents , Cost , ProductProd , HistoriOfTheOtchet
from .forms import ItapApdete , ItapAP, UploadFileForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail , send_mass_mail
from resurses.models import Otdel ,Zadatha , Contacts ,Cotrudniri , Compani , PriseofmyWok ,OtchetforMonf 
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime , timedelta 
import openpyxl
import pytz
import calendar

from django.contrib.auth.decorators import login_required

# Create your views here.

def otchet_new(request):
    itap = Itap.objects.all()
    proj = Projects.objects.filter(otchtetm='Д').exclude(activedog = "Завершен").exclude(activedog = "Системный")
    return render(request, 'projects/otchet-new.html',{'projects':proj,'itap':itap})

# Все проекты отчет общий (без редактироания)
def dashbotrd_pass(request):
    itap = Itap.objects.all()
    proj = Projects.objects.exclude(activedog = "Завершен").exclude(activedog = "Системный")
    return render(request, 'projects/prodject-dashbord-pass.html',{'projects':proj,'itap':itap})
# Редактироание Паспартов
def pasport_red(request,pk):
    projects = get_object_or_404(Projects, id=pk)
    comp = Compani.objects.all()
    try:
        compannn = Compani.objects.get(id=projects.compani)
    except:
        compannn = {"title":"-"}
    #otdel = Otdel.objects.filter(projects__title=projects).first()
    users = User.objects.all()
    itap= Itap.objects.filter(projects__title=projects)
    if request.method == 'POST':
        dd = request.POST.get('form')
        if dd == "newcompani":
            c = Compani()
            c.title = request.POST.get('title')
            c.opisanie = request.POST.get('otvet')
            c.save()
            c = Compani.objects.get(title=request.POST.get('title'))
            pr = Projects.objects.get(id= pk)
            pr.compani = c.id
            pr.save()

        else:
            itid = request.POST.getlist('itid')
            datastart = request.POST.getlist('datastart')
            datastop = request.POST.getlist('datastop')
            itapnaim = request.POST.getlist('itapnaim')
            itaptitle =  request.POST.getlist('itaptitle')
            g = 0
            for i in itid:
                try:
                    it = Itap.objects.get(id= i)
                
                    it.datastart =  datastart[g]
                    it.datastop =  datastop[g]
                    it.itapnaim = itapnaim[g]
                    it.title = itaptitle[g]
                    it.save()
                    try:
                        mo = Mani.objects.get(itap= it )
                    except:
                        mo = Mani()
                        mo.title = it.title
                        mo.itap = it
                        mo.save()
                    g= g+1
                except:
                    g= g+1

            titlenew = request.POST.get('titlenew')
            itapnaimnew = request.POST.get('itapnaimnew')
            datastartnew = request.POST.get('datastartnew')
            datastopnew = request.POST.get('datastopnew')
            pr = Projects.objects.get(id= pk)

            if titlenew != ' ':
                try:
                    #str(str(int(a[2]))+'-'+a[1]+'-'+a[0])
                    #str(str(int(b[2]))+'-'+b[1]+'-'+b[0])
                    #a = datastartnew.split('.')
                    #b = datastopnew.split('.')
                    it = Itap()
                    it.title = titlenew
                    it.itapnaim = itapnaimnew
                    it.datastart = datastartnew
                    it.datastop = datastopnew
                    it.komentrp =  ''
                    it.komentstep = '' 
                    it.projects = pr
                    it.save()

                except:
                    pass
            else:
                pass

            pr.nomerdogovora = request.POST.get('nomerdogovora') 
            pr.rpproecta = request.POST.get('rpproecta')
            pr.sistema = request.POST.get('sistema')
            pr.prisezatrat = request.POST.get('prisezatrat')
            pr.prisepr = request.POST.get('prisepr')
            pr.tipdogovora = request.POST.get('tipdogovora')
            

            zakazchic = request.POST.get('zakazchic')
            if zakazchic == "None" or zakazchic == "-":
                pass
            else:
                pr.compani = zakazchic
            pr.save()

        return redirect('projects:myprod') 

    return render(request, 'projects/prodject-dashbord-pasport-rename.html',{ "users":users, "projects":projects,'itap':itap ,'comp':comp ,'compannn':compannn})
# ПМО главная 
def pmo_main_page(request):
    use = User.objects.all()
    return render(request, 'projects/prodject-pmo.html',{'use':use})
# ПМО рассылка 
def pmo_post_page(request):
    use = User.objects.all()
    mails = []
    for e in use:
        if e.email == '':
            pass
        else:
            mails.append(e.email)
    try:
        mails.append('makeev.m@galaktika.ru')
        send_mail(
                '[Системы РМО] Отчет по проектам',
                'Добрый день, коллеги.\r\n  \r\n Прошу обновить статус отчет по Вашим проектам на портале: https://ru01-app38.galaktika.ru/',
                'system.pmo@galaktika.ru',
                mails,
                fail_silently=False,
                
                )
        post = "Сообщения отправлены"
    except:
        post = "Сообщения HE отправлены "
        
    return render(request, 'projects/prodject-pmo.html', {'post':post,'use':use})
# выйти
def logout_view(request):
    success_url = reverse_lazy('projects:ligin')
    logout(request)
    return redirect(success_url)
# Войти 
def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                return redirect('projects:myprod')
            else: 
                return redirect('projects:ligin')
        except:
            return redirect('projects:ligin') 
    return render(request, 'projects/prodject-login.html' )
# Все проекты (Отчеты)

@login_required(login_url='/lg/')
def projects_views_all(request):
    itap = Itap.objects.all()
    proj = Projects.objects.exclude(activedog__in = ["Завершен", "Системный"])
    if request.method == 'POST':
        proj = proj.filter(title__startswith=request.POST.get('s'))
        return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap })
    return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap})
#  Все проекты / Мои проекты (отчеты)
@login_required(login_url='/lg/')
def projects_views(request):
    try:
        if request.user.username == 'stepanova' or request.user.username == 'boss' or request.user.username == 'malkov' :
            itap = Itap.objects.all()
            proj = Projects.objects.filter(Q(activedog ="В работе") | Q(activedog ="Приостановлен"))
            if request.method == 'POST':
                proj = proj.filter(title__startswith=request.POST.get('s'))
                return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap })
            return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap })
        else:
            proj = Projects.objects.filter(rpproecta=request.user.first_name).filter(Q(activedog ="В работе") | Q(activedog ="Приостановлен"))
            itap = Itap.objects.all()
            if request.method == 'POST':
                proj = proj.filter(title__startswith=request.POST.get('s'))
                return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap })
            return render(request, 'projects/prodject-dashbord.html',{'projects':proj,'itap':itap })    
    except:
        return redirect('projects:ligin')
#   Отчет М    
def otchet(request): 
    itap = Itap.objects.all()
    proj = Projects.objects.exclude(activedog = "Системный")
    otch = 'Д'
    
    return render(request, 'projects/otchet.html',{'projects':proj,'itap':itap,'otch':otch })
# Возможность редактироать все проекты (Доработаь ) _______ПЕРЕПИСАТЬ 
@login_required(login_url='/lg/')
def list_otch(request):
    itap = Itap.objects.all()
    proj = Projects.objects.exclude(activedog = "Системный")
    
    if request.method == 'POST':
        form =ItapAP(request.POST)
        otchm = request.POST.getlist('otchm')
        step = request.POST.getlist('komentstep')
        rpot = request.POST.getlist('komentrp')
        zad = request.POST.getlist('zadolkjnost')
        itapid = request.POST.getlist('iditap')

        if form.is_valid():
            vin = 0
            for k in proj:
                pro = Projects.objects.get(id=k)
                pro.otchtetm = otchm[vin]
                pro.save()
                vin=vin+1

            vid = 0
            for ot in itapid:
                try:
                    ots = Itap.objects.get(id=ot)
                    ots.komentstep =step[vid]
                    ots.komentrp = rpot[vid]
                    ots.zadolkjnost = zad[vid]
                    ots.save()
                    vid=vid+1
                except:
                    vid=vid+1
                    print(ot)

        return redirect('projects:views')
    return render(request, 'projects/prodject-pmo-vseproecty.html',{'projects':proj,'itap':itap})
# Проверка обновления _______ПЕРЕПИСАТЬ
@login_required(login_url='/lg/')
def check(request):
    proj = Projects.objects.all()
    fad =[]
    for pr in proj:
        fad.append(pr.rpproecta)
    rp = list(set(fad))
    rp.sort()
    if request.method == 'POST':
        use = User.objects.all()
        browser = request.POST.getlist('browser')
        mails = []
        cou = 0
        for emll in browser:
            try:
                mm = use.get(first_name=emll).email
                if emll == '':
                    print('1')
                else:
                    mails.append(mm)
                    cou = cou + 1
            except:
                pass

        emaai = "Сообщений отправленно: " + str(cou)
        mails.append('makeev.m@galaktika.ru')
        send_mail(
                '[Системы РМО] Отчет по проектам',
                'Добрый день, коллеги.\r\n  \r\n Прошу обновить статус отчет по Вашим проектам на портале: https://ru01-app38.galaktika.ru/',
                'system.pmo@galaktika.ru',
                mails,
                fail_silently=False,
                )

        return render(request, 'projects/prodject-pmo-chec.html',{ 'rp':rp , 'emaai': emaai ,'proj':proj })
    return render(request, 'projects/prodject-pmo-chec.html',{ 'rp':rp ,'proj':proj})
# Мои проекты 
@login_required(login_url='/lg/')
def dashboard_myprod(request):
    if  request.user.username == 'boss' or request.user.username == 'malkov' :
        prom = Projects.objects.exclude(activedog = "Системный")
    else:
        prom = Projects.objects.filter(rpproecta=request.user.first_name).exclude(activedog = "Системный")
    return render(request, 'projects/prodject-allprod.html',{'projects':prom})
# Все проекты 
@login_required(login_url='/lg/')
def dashboard_allprod(request):
    success_url= reverse_lazy('projects:allprod')
    prom = Projects.objects.all()
    
    if request.method == 'POST':
        iditm = request.POST.getlist('iditm')
        activedog = request.POST.getlist('activedog')
        otchm = request.POST.getlist('otchm')
        d = 0
        now = datetime.now().date()
        for i in iditm:
            
            pr = Projects.objects.get(id = i)
            pr.activedog = activedog[d]
            pr.otchtetm = otchm[d]
            pr.save()
            d = d+1 
            
            try:
                if pr.tipdogovora == 'Методологическое сопровождение(А)'or pr.tipdogovora =='Техническое сопровождение':
                    ita = Itap.objects.filter(projects__id=i).last()
                    b = str(now)
                    b = b.split('-')
                    fo = calendar.monthrange(int(b[0]),int(b[1]))
                    if now >= ita.datastop:
                        d1 = ita.title.split(' ')
                        it = Itap()
                        it.projects = pr
                        it.title = d1[0] +" " +str(int(d1[1]) + 1)
                        it.datastart = str(b[0]+'-'+ b[1] +'-01')
                        it.datastop = str(b[0]+'-'+b[1] +'-'+ str(fo[1]))
                        it.komentstep =""
                        it.komentrp = ""
                        it.itapnaim = ita.itapnaim 
                        it.oplata = "В работе"
                        it.act = "В работе"
                        it.save()
            except :
                pass

        return redirect(success_url)

    return render(request, 'projects/prodject-myprod.html',{'projects':prom})
# Паспорт проекта 
@login_required(login_url='/lg/')
def dashboard_pasport(request,pk):
    proj = get_object_or_404(Projects,id=pk)
    try:
        comp = Compani.objects.get(id=proj.compani)
    except:
        comp = {"title":"-"}

    compa = Compani.objects.all()
    prod =  ProductProd.objects.all()
    
    histori = HistoriOfTheOtchet.objects.filter(projects__id=pk)
    #otdel = Otdel.objects.filter(projects__title=proj).first()
    itap = Itap.objects.filter(projects__title=proj)
    zadan = Zadania.objects.filter(itap__projects__title=proj)
    #komand = Komanda.objects.filter(projects__title=proj)
    dopsogl = Dopsog.objects.filter(projects__title=proj)
    riskss = Risk.objects.filter(projects__title=proj)
    prob = Problems.objects.filter(projects__title=proj)
    cost = Cost.objects.filter(projects__title=proj)
    mone = Mani.objects.filter(itap__projects__title=proj)
    docs = Documents.objects.filter(itap__projects__title=proj)
    zada = Zadatha.objects.filter(projects__title=proj)
    cont = Cotrudniri.objects.filter(projects__title=proj).filter(tip='sotrudnic').exclude(statusof='Уволен')
    contac = Cotrudniri.objects.exclude(projects__title=proj).filter(tip='sotrudnic').exclude(statusof='Уволен')
    users = User.objects.all()

    
    #komadamodel = list(PriseofmyWok.objects.filter(projects__id=pk).values_list('otch_id', flat=True).distinct())
    #komadamodel = OtchetforMonf.objects.all()[:6]
    komadamodel = OtchetforMonf.objects.all().order_by('-id')

    if request.method == 'POST':
        prov =  request.POST.get('prov')
        if prov == "team":
            o =0
            dpds = request.POST.getlist('checid')
            gor = OtchetforMonf.objects.all().last()
            for i in request.POST.getlist('proz'):
                if i == '-':
                    o =o+1 
                else:
                    try:
                        pr = PriseofmyWok.objects.filter(projects__id=dpds[o].split('?')[0]).filter(cotrud__index=dpds[o].split('?')[1]).filter(otch=gor).get()
                        pr.title = i
                        pr.save()
                        o =o+1 
                    except:
                        pr = PriseofmyWok()
                        pr.projects = Projects.objects.get(id =dpds[o].split('?')[0])
                        pr.cotrud = Cotrudniri.objects.get(index=dpds[o].split('?')[1])
                        pr.otch = gor
                        pr.title = i
                        #if Itap.objects.filter(projects__id=dpds[o].split('?')[0]).exclude(act='Подписан').first() == None:
                        #    pr.itap = Itap.objects.filter(projects__id=dpds[o].split('?')[0]).last()
                        #else:
                        #    pr.itap = Itap.objects.filter(projects__id=dpds[o].split('?')[0]).exclude(act='Подписан').first() 
                        pr.save()
                        o =o+1 
        elif prov == "searshcotrud":
            contac = Cotrudniri.objects.exclude(projects__title=proj).filter(title__startswith=request.POST.get('s'))

            return render(request, 'projects/prodject-dashbord-pasport.html',{'contac':contac, 'komadamodel':komadamodel ,'zada':zada,'projects':proj,'itap':itap,'dopsogl':dopsogl,'komand':cont ,'zadat':zadan ,'prob':prob,'riskss':riskss ,'mone':mone ,'docs':docs, "cost":cost ,'comp':comp ,'idollcontacts':'ollcontacts'})

        elif prov == "otshet":
            ide = request.POST.getlist('idit')
            pol = request.POST.getlist('komentrp')
            acts = request.POST.getlist('act')
            oplatas = request.POST.getlist('oplata')
            zadolkjnost = request.POST.getlist('zadolkjnost') 
            vin = 0
            for i in ide:
                proj = Itap.objects.get(id=i)
                if proj.komentrp !=  pol[vin]:
                    his = HistoriOfTheOtchet()
                    his.title = proj.title
                    his.projects = Projects.objects.get(id = proj.projects.id )
                    his.name = request.user.first_name
                    his.oldkomentrp = pol[vin]
                    his.save()
                else:
                    pass
                proj.oldkomentrp = proj.komentrp
                proj.komentrp = pol[vin]
                proj.oplata = oplatas[vin]
                proj.act = acts[vin]
                proj.zadolkjnost = zadolkjnost[vin]
                proj.save()
                vin=vin+1

        elif prov =='adcontact':
            de = request.POST.getlist('addcontsct')

            try:
                for i in de: 
                    contac = Cotrudniri.objects.get(index =i)
                    contac.projects.add(proj)
                    contac.save()
            except:
                pass

        elif prov == "zadatcha":
            try:
                itmm = request.POST.getlist('itmm') 
                prozentviponenia = request.POST.getlist('prozentviponenia')
                n=0
                for i in itmm:
                    zad = Zadania.objects.get(id = i)
                    zad.prozes = prozentviponenia[n]
                    zad.save()
                    n=n+1
            except:
                pass

        elif prov == "risc":  
            try:
                title = request.POST.getlist('title')
                seryznost = request.POST.getlist('seryznost')
                veroyt = request.POST.getlist('veroyt')
                koment = request.POST.getlist('koment')
                proms = proj
                n = 0
                for i in title:
                    kom = Risk()
                    kom.projects = proms
                    kom.title = i
                    kom.serios = seryznost[n] 
                    kom.status = veroyt[n] 
                    kom.koment = koment[n] 
                    kom.save()
                    n=n+1
            except:
                pass

            try:
                iddd = request.POST.getlist('iddd')
                titlee = request.POST.getlist('titlee')
                serios = request.POST.getlist('serios')
                status = request.POST.getlist('status')
                komente = request.POST.getlist('komente')
                n = 0
                for i in iddd:
                    dat = Risk.objects.get(id=i)
                    dat.title = titlee[n]
                    dat.serios = serios[n]
                    dat.status = status[n]
                    dat.koment= komente[n]
                    dat.save()
                    n = n + 1
            except:
                pass

        elif prov == "problem":
            try:
                title = request.POST.getlist('title')
                seryznost = request.POST.getlist('seryznost')
                veroyt = request.POST.getlist('veroyt')
                koment = request.POST.getlist('koment')
                proms = Projects.objects.get(id=pk)
                n = 0
                for i in title:
                    kom = Problems()
                    kom.projects = proms
                    kom.title = i 
                    kom.serios = seryznost[n] 
                    kom.status = veroyt[n] 
                    kom.koment = koment[n] 
                    kom.save()
                    n=n+1
            except:
                pass
            try:
                iddd = request.POST.getlist('iddd')
                titlee = request.POST.getlist('titlee')
                serios = request.POST.getlist('serios')
                status = request.POST.getlist('status')
                komente = request.POST.getlist('komente')
                n = 0
                for i in iddd:
                    dat = Problems.objects.get(id=i)
                    dat.title = titlee[n]
                    dat.serios = serios[n]
                    dat.status = status[n]
                    dat.koment= komente[n]
                    dat.save()
                    n = n + 1
            except:
                pass
                
        elif prov == "doc":
            try:
                idold = request.POST.getlist('idold')
                titleold = request.POST.getlist('titleold')
                plandataold = request.POST.getlist('plandataold')
                statusdocold = request.POST.getlist('statusdocold')
                f = 0
                for doc in idold:
                    do = Documents.objects.get(id = doc)
                    do.title = titleold[f]
                    do.status = statusdocold[f]
                    a = plandataold[f].split('.')
                    do.data = str(str(int(a[2]))+'-'+a[1]+'-'+a[0])
                    do.save()
                    f = f+1

            except:
                pass

            try:
                iddd = request.POST.getlist('iddd')
                doctitle = request.POST.getlist('doctitle')
                datadoc = request.POST.getlist('datadoc')
                statusdoc = request.POST.getlist('statusdoc')
                
                d = 0
                for i in iddd:
                    it = Itap.objects.get(id=i)
                    do = Documents()
                    do.title = doctitle[d]
                    do.itap = it
                    do.status = statusdoc[d]
                    a = datadoc[d].split('.')
                    do.data = str(str(int(a[2]))+'-'+a[1]+'-'+a[0])
                    do.save()
                    d = d+1
            except:
                pass

        elif prov == "prise":
            obshay = request.POST.getlist('obshay')
            avanse = request.POST.getlist('avanse')
            ozhidaem = request.POST.getlist('ozhidaem')
            stasuss = request.POST.getlist('stasuss')
            idd = request.POST.getlist('idd')
            f = 0
            for i in idd:
                mo = Mani.objects.get(id=i)
                mo.title =obshay[f]
                mo.avanse = avanse[f]
                mo.status = stasuss[f]
                if ozhidaem[f] != '':
                    mo.data = datetime.strptime(ozhidaem[f], "%d.%m.%Y") 
                else:
                    pass
                mo.save()
                f=f+1
        elif prov == "cost":
            title = request.POST.get('title')
            cost = request.POST.get('serios')
            if title != "" or cost != "":
                co = Cost()
                co.title = title
                co.serios = cost
                co.projects = proj
                co.save()
            else:
                pass

        elif prov  == 'products':
            press = Projects.objects.get(id = pk) 
            idlist = request.POST.getlist('addcontsct') 
            press.products.clear()
            press.save()
            for i in idlist:
                press.products.add(ProductProd.objects.get(id=i))
            press.save()

        elif prov  == 'newcompani':
            c = Compani()
            c.title = request.POST.get('title')
            c.opisanie = request.POST.get('otvet')
            c.save()
            c = Compani.objects.get(title=request.POST.get('title'))
            pr = Projects.objects.get(id= pk)
            pr.compani = c.id
            pr.save()
        
        elif prov  == 'nastroikios':
            itid = request.POST.getlist('itid')
            datastart = request.POST.getlist('datastart')
            datastop = request.POST.getlist('datastop')
            itapnaim = request.POST.getlist('itapnaim')
            itaptitle =  request.POST.getlist('itaptitle')
            g = 0
            for i in itid:
                try:
                    it = Itap.objects.get(id= i)
                
                    it.datastart =  datastart[g]
                    it.datastop =  datastop[g]
                    it.itapnaim = itapnaim[g]
                    it.title = itaptitle[g]
                    it.save()
                    try:
                        mo = Mani.objects.get(itap= it )
                    except:
                        mo = Mani()
                        mo.title = it.title
                        mo.itap = it
                        mo.save()
                    g= g+1
                except:
                    g= g+1

            titlenew = request.POST.get('titlenew')
            itapnaimnew = request.POST.get('itapnaimnew')
            datastartnew = request.POST.get('datastartnew')
            datastopnew = request.POST.get('datastopnew')
            pr = Projects.objects.get(id= pk)

            if titlenew != ' ':
                try:
                    it = Itap()
                    it.title = titlenew
                    it.itapnaim = itapnaimnew
                    it.datastart = datastartnew
                    it.datastop = datastopnew
                    it.komentrp =  ''
                    it.komentstep = '' 
                    it.projects = pr
                    it.save()
                except:
                    pass
            else:
                pass

            pr.nomerdogovora = request.POST.get('nomerdogovora') 
            pr.rpproecta = request.POST.get('rpproecta')
            
            pr.prisezatrat = request.POST.get('prisezatrat')
            pr.prisepr = request.POST.get('prisepr')
            pr.tipdogovora = request.POST.get('tipdogovora')
            pr.activedog = request.POST.get('activedog')

            zakazchic = request.POST.get('zakazchic')
            if zakazchic == "None" or zakazchic == "-":
                pass
            else:
                pr.compani = zakazchic
            pr.save()

        else:   
            pass

        return redirect("/proect/%s/" % (pk)) #,'otdel':otdel
    return render(request, 'projects/prodject-dashbord-pasport.html',{'users':users, 'histori':histori, 'prod':prod, 'contac':contac, 'compa':compa,'komadamodel':komadamodel,'zada':zada,'projects':proj,'itap':itap,'dopsogl':dopsogl,'komand':cont ,'zadat':zadan ,'prob':prob,'riskss':riskss ,'mone':mone ,'docs':docs, "cost":cost ,'comp':comp})

# Оперплан  _______ПЕРЕПИСАТЬ
@login_required(login_url='/lg/')
def dashboard_operplan(request,pk):
    success_url= reverse_lazy('projects:myprod')
    prom = Projects.objects.all()
    proj = prom.filter(id=pk)
    itap = Itap.objects.filter(projects__title=prom.get(id=pk))
    zadan = Zadania.objects.filter(itap__projects__title=prom.get(id=pk))
    
    if request.method == 'POST':

        itphiden = request.POST.getlist('itapid')
        punktplana = request.POST.getlist('punktplana')
        datafi = request.POST.getlist('datafi')
        dataend = request.POST.getlist('dataend')
        rezuls = request.POST.getlist('rezuls')
        document = request.POST.getlist('document')

        k = []
        g = 0 
        for ert in itphiden:
            try:
                zaazz = Itap.objects.get(id=ert)
                k.append(ert)
            except:
                zaazz = Itap.objects.get(id=k[-1])
                zad = Zadania()
                zad.rezult = rezuls[g]
                zad.documentrez = document[g]
                zad.title = punktplana[g]
                if dataend[g] != '':
                    zad.data = datetime.strptime(datafi[g], "%d.%m.%Y") 
                else:
                    pass
                if datafi[g] != '':
                    zad.data = datetime.strptime(dataend[g], "%d.%m.%Y") 
                else:
                    pass
                zad.itap = zaazz 
                zad.save()
                g = g + 1 
        
        imm = request.POST.getlist('imm')
        title = request.POST.getlist('title')
        level = request.POST.getlist('level')
        datee = request.POST.getlist('datee')
        dateend = request.POST.getlist('dateend')
        rezall = request.POST.getlist('rezall') 
        document = request.POST.getlist('document')
        g=0
        for re in imm: 
            zaz = Zadania.objects.get(id=re)
            zaz.title = title[g]
            zaz.level = level[g]
            
            if datee[g] != '':
                zaz.data = datetime.strptime(datee[g], "%d.%m.%Y")  
            else:
                pass

            if dateend[g] != '':
                zaz.dataend = datetime.strptime(dateend[g], "%d.%m.%Y")  
            else:
                pass
            
            zaz.rezult = rezall[g]
            zaz.documentrez =  document[g]
            zaz.save()
            g=g+1


        return redirect("/proect/%s/" % (pk))
    return render(request, 'projects/prodject-operplan.html',{'projects':proj,'itap':itap,'zadat':zadan})
# Отчет редактирование Степанова 
@login_required(login_url='/lg/')
def projects_detail_st_low(request,pk):
    prom = Projects.objects.get(id=pk)
    itap = Itap.objects.filter(projects__title=prom)
    nom = len(itap)  

    if request.method == 'POST':
        form =ItapAP(request.POST)
        pol = request.POST.getlist('komentstep')
        acts = request.POST.getlist('act')
        oplatas = request.POST.getlist('oplata')
        idid = request.POST.getlist('idid')
        zadolkjnost = request.POST.getlist('zadolkjnost')
        if form.is_valid():
            vin = 0
            for i in idid:
                proj = Itap.objects.get(id=i)

                if proj.zadolkjnost != zadolkjnost[vin]:
                    his = HistoriOfTheOtchet()
                    his.title = proj.title
                    his.projects = Projects.objects.get(id = proj.projects.id )
                    his.name = request.user.first_name
                    his.oldkomentrp = zadolkjnost[vin]
                    his.save()
                else:
                    pass
                proj.oplata = oplatas[vin]
                proj.act = acts[vin]
                proj.komentstep = pol[vin]
                proj.zadolkjnost = zadolkjnost[vin]
                proj.save()
                vin=vin+1
            return redirect("/#%s" % (pk))
    
    return render(request, 'projects/prodject-detail-st.html',{'projects':prom,'itap':itap,'nom': nom })
# Отчет пердактирование 
@login_required(login_url='/lg/')
def projects_detail(request,pk):
    prom = Projects.objects.get(id=pk)
    itap = Itap.objects.filter(projects__title=prom)
    nom = len(itap)    

    if request.method == 'POST':
        pol = request.POST.getlist('komentrp')
        acts = request.POST.getlist('act')
        oplatas = request.POST.getlist('oplata')
        zadolkjnost = request.POST.getlist('zadolkjnost')
        vin = 0
        for i in itap:
            proj = i
            if proj.komentrp !=  pol[vin]:
                his = HistoriOfTheOtchet()
                his.title = proj.title
                his.projects = Projects.objects.get(id = proj.projects.id )
                his.name = request.user.first_name
                his.oldkomentrp = pol[vin]
                his.save()
            else:
                pass
            proj.oldkomentrp = proj.komentrp
            proj.komentrp = pol[vin]
            proj.oplata = oplatas[vin]
            proj.act = acts[vin]
            proj.zadolkjnost = zadolkjnost[vin]
            proj.save()
            vin=vin+1
        return redirect("/#%s" % (pk))
    return render(request, 'projects/prodject-detail.html',{'projects':prom,'itap':itap,'nom': nom })

# Дашборд ___________! переписать нах постом

def deshbord_prodj(request):
    pro = Projects.objects.exclude(activedog = "Системный")
    prb = Problems.objects.all()
    ris = Risk.objects.all()
    it = Itap.objects.all()

    ms = 0
    ts = 0
    vnut = 0
    vnedr = 0
    
    # "ms":ms,'ts':ts,'vnut':vnut,"vnedr",vnedr
    name=[]
    cost = []
    osvoe = []
    for red in pro:
        name.append(red.title[0:12])
        try:
            cost.append(int(red.prisepr))
            osvoe.append(int(red.osvoeno))
        except :
            osvoe.append(int(0))
            cost.append(int(0))

        if red.tipdogovora == 'Методологическое сопровождение':
            ms =ms+1
        elif red.tipdogovora == 'Внедрение': 
            vnedr =vnedr+1
        elif red.tipdogovora == "Внутренний проект":
            vnut =vnut +1
        elif red.tipdogovora == 'Техническое сопровождение':
            ts =ts+1
        else:
            vnedr =vnedr+1
            
               
    opla = 0
    ojid = 0
    zadol = 0

    for i in it:
        if i.oplata == "Оплачен":
            opla = opla+1
        elif i.oplata == "Ожидаем":
            ojid = ojid +1
        elif i.oplata == "Задолжность":
            zadol = zadol +1
        else:
            pass
    olinfo = [int(prb.count()),int(ris.count()),int(opla),int(ojid) ,int(zadol)]
    return render(request, 'projects/prodject-dash-proect.html',{'projects':pro ,'prob':prb,"name":name,"cost":cost ,'osvoe':osvoe,'olinfo':olinfo, "ms":ms,'ts':ts,'vnut':vnut,"vnedr":vnedr})

@login_required(login_url='/lg/')
def dashbord_pocaz(request,pk):
    prom = Projects.objects.get(id=pk)

    return render(request, 'projects/prodject-pokaz.html',{'projects':prom })
    
@login_required(login_url='/lg/')
def del_sotr_from(request, pk, cot):
    p2 = Projects.objects.get(id = pk )
    contac = Cotrudniri.objects.get(index =cot)
    contac.projects.remove(p2)
    contac.save()
    return redirect("/proect/%s/" % (pk))  


