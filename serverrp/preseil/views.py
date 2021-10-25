from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from preseil.models import PresailProjects, StadiiProdaj ,KomentForPresail ,  ProductOf  , PresProjNew
from django.contrib.auth.models import User
from resurses.models import Compani , Cotrudniri , PriseofmyWok , OtchetforMonf
from projects.models import ProductProd
# Create your views here.

@login_required(login_url='/lg/')
def preseilmainall(request):
    press = PresProjNew.objects.exclude(status='Отказ').exclude(status='Завершен')
    use = User.objects.all()
    prod = ProductProd.objects.all() 
    if request.method == 'POST':
        rp = request.POST.get('rp')
        products = request.POST.get('product')
        polzvt = request.POST.get('polzvt') 
        status = request.POST.get('status')
        #sum1 = request.POST.get('sum1')
        #sum2 = request.POST.get('sum2')
        #kanal = request.POST.get('kanal') 
        if polzvt !='-' and status != '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(polzvt=polzvt).filter(products=products)

        elif polzvt =='-' and status == '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(products=products)
        elif polzvt =='-' and status == '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp)
        elif polzvt =='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status)
        elif polzvt !='-' and status == '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(polzvt=polzvt)

        elif polzvt =='-' and status != '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(products=products)
        elif polzvt !='-' and status == '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(polzvt=polzvt)

        elif polzvt =='-' and status == '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(products=products)
        elif polzvt !='-' and status == '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt)
        elif polzvt =='-' and status != '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status)

        elif polzvt =='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(products=products)
        elif polzvt !='-' and status == '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(polzvt=polzvt)
        elif polzvt =='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt)


        else:
            press = PresProjNew.objects.all()


        #press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status)
        return render(request, 'presail/prodject-presail-all.html',{'press':press , 'users':use ,'prod':prod })

    return render(request, 'presail/prodject-presail-all.html',{'press':press , 'users':use ,'prod':prod })

@login_required(login_url='/lg/')
def preseilmainmy(request): 
    use = User.objects.all()
    prod = ProductProd.objects.all() 
    press = PresProjNew.objects.exclude(status='Отказ').exclude(status='Завершен').filter(rpproecta=request.user.first_name)

    if request.method == 'POST':
        rp = request.POST.get('rp')
        products = request.POST.get('product')
        polzvt = request.POST.get('polzvt') 
        status = request.POST.get('status')
        #sum1 = request.POST.get('sum1')
        #sum2 = request.POST.get('sum2')
        #kanal = request.POST.get('kanal') 
        if polzvt !='-' and status != '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(polzvt=polzvt).filter(products=products)

        elif polzvt =='-' and status == '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(products=products)
        elif polzvt =='-' and status == '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp)
        elif polzvt =='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status)
        elif polzvt !='-' and status == '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(polzvt=polzvt)

        elif polzvt =='-' and status != '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(products=products)
        elif polzvt !='-' and status == '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status).filter(polzvt=polzvt)

        elif polzvt =='-' and status == '-' and rp != '-' and products != '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(products=products)
        elif polzvt !='-' and status == '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(polzvt=polzvt).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt)
        elif polzvt =='-' and status != '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status)

        elif polzvt =='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(products=products)
        elif polzvt !='-' and status == '-' and rp != '-' and products == '-':
            press = PresProjNew.objects.filter(rpproecta=rp).filter(polzvt=polzvt)
        elif polzvt =='-' and status != '-' and rp == '-' and products != '-':
            press = PresProjNew.objects.filter(status=status).filter(products=products)
        elif polzvt !='-' and status != '-' and rp == '-' and products == '-':
            press = PresProjNew.objects.filter(status=status).filter(polzvt=polzvt)


        else:
            press = PresProjNew.objects.all()


        #press = PresProjNew.objects.filter(rpproecta=rp).filter(status=status)
        return render(request, 'presail/prodject-presail-all.html',{'press':press , 'users':use ,'prod':prod })

    return render(request, 'presail/prodject-presail-all.html',{'press':press , 'users':use ,  'prod':prod})

@login_required(login_url='/lg/')
def preseilnew(request):
    use = User.objects.all()
    comp = Compani.objects.all()

    if request.method == 'POST':
        press = PresProjNew()
        press.title = request.POST.get('title') 
        press.kanal = request.POST.get('kanal') 
        press.summa = request.POST.get('prisezatrat')
        press.kontrok = request.POST.get('kontrok')
        press.polzvt = request.POST.get('polzvt')
        press.status = request.POST.get('status')
        press.rpproecta = request.POST.get('rpproecta')
        press.rucgrup = "pres"
        press.activedog = "Системный"
        press.save()

        st = StadiiProdaj()
        st.title =request.POST.get('title') 
        st.priailnnew = press
        st.save()
        return redirect('preseil:presail') 
    return render(request, 'presail/prodject-presail-new.html',{'users':use, "comp":comp})

@login_required(login_url='/lg/')
def preseilmain(request, pk):
    press =  PresProjNew.objects.get(id=pk)
    stadi =  StadiiProdaj.objects.get(priailnnew=press)
    koment = KomentForPresail.objects.filter(priailnnew=press)
    comp = Compani.objects.all()
    use = User.objects.all()
    compan = Compani.objects.filter(id=press.compani).first()
    prod = ProductProd.objects.all() 
    cont = Cotrudniri.objects.filter(projects=press).filter(tip='sotrudnic').exclude(statusof='Уволен')
    contac = Cotrudniri.objects.exclude(projects=press).filter(tip='sotrudnic').exclude(statusof='Уволен')
    #piseof = PriseofmyWok.objects.filter(projects=press)
    #komadamodel = list(PriseofmyWok.objects.filter(projects=press).values_list('otch_id', flat=True).distinct())
    
    komadamodel = OtchetforMonf.objects.all()[:6]

    if request.method == 'POST':
        tip = request.POST.get('tip')
        if tip == "stadii":
            status = request.POST.getlist('status')
            textar = request.POST.getlist('textsname')
            stadi.znacomstvostatus = status[0]
            stadi.znacomstvo = textar[0]
            stadi.pismostatus = status[1]
            stadi.pismo = textar[1]
            stadi.vstrethastatus = status[2]
            stadi.vstretha = textar[2]
            stadi.napravleniastatus = status[3]
            stadi.napravlenia = textar[3]
            stadi.kartadorogstatus = status[4]
            stadi.kartadorog = textar[4]
            stadi.obsledstatus = status[5]
            stadi.obsled = textar[5]
            stadi.orgvoprosstatus = status[6]
            stadi.orgvopros = textar[6]
            stadi.interviustatus = status[7]
            stadi.interviu = textar[7]
            stadi.otchetstatus = status[8]
            stadi.otchet = textar[8]
            stadi.zachitaotchstatus = status[9]
            stadi.zachitaotch = textar[9]
            stadi.formirovaniepredstatus = status[10]
            stadi.formirovaniepred = textar[10]
            stadi.predlojeniestatus = status[11]
            stadi.predlojenie = textar[11]
            stadi.soglosovaniezactatus = status[12]
            stadi.soglosovanie = textar[12]
            stadi.soglosovaniezacstatus = status[13]
            stadi.soglosovaniezac = textar[13]
            stadi.obratnazsvazstatus = status[14]
            stadi.obratnazsvaz = textar[14]
            stadi.predlojeniestatusitog = status[15]
            stadi.predlojenieitog = textar[15]
            stadi.konkyrsnazdocstatus = status[16]
            stadi.konkyrsnazdoc = textar[16]
            stadi.konkursstatus = status[17]
            stadi.konkurs = textar[17]
            stadi.save()

        # Доделать   
        elif tip  == 'newcompani':
            co = Compani()
            co.title =request.POST.get('title') 
            co.opisanie =request.POST.get('otvet') 
            co.save()
            press.compani = Compani.objects.get(title= request.POST.get('title')).id
            press.save()
        
        # Отчет
        elif tip  == 'otsh':
            kom = KomentForPresail()
            kom.title = request.user.first_name
            kom.koment = request.POST.get('statusnew') 
            kom.plan = request.POST.get('statusplan')
            kom.statuschek =  request.POST.get('statuschek')
            kom.priailnnew = press 
            kom.save()
        
        # Продукты
        elif tip  == 'products':
            idlist = request.POST.getlist('addcontsct') 
            press.products.clear()
            press.save()
            for i in idlist:
                press.products.add(ProductProd.objects.get(id=i))
            press.save()

        # Переименовать     
        elif tip  == 'renemeof':
            press =  PresProjNew.objects.get(id=pk)
            press.title = request.POST.get('title') 
            press.kanal = request.POST.get('kanal') 
            press.summa = request.POST.get('prisezatrat')
            #press.product = request.POST.get('product')
            press.kontrok = request.POST.get('kontrok')
            press.polzvt = request.POST.get('polzvt')
            press.status = request.POST.get('status')
            if  request.POST.get('status') == "Отказ" or  request.POST.get('status')== 'Завершен':
                press.activedog = "Завершен"
            press.veroytnost = request.POST.get('veroytnost')
            press.rpproecta = request.POST.get('rpproecta')
                
            zakazchic = request.POST.get('zakazchic')
            if zakazchic == "None" or zakazchic == "-" or  zakazchic == "":
                pass
            else:
                press.compani = zakazchic
            press.save()

        # Мои контакты 
        elif tip =='adcontact':
            de = request.POST.getlist('addcontsct')
            try:
                for i in de: 
                    contac = Cotrudniri.objects.get(index =i)
                    contac.projects.add(press)
                    contac.save()
            except:
                pass   
        # Поиск
        elif tip == "searshcotrud":
            contac = Cotrudniri.objects.exclude(projects=press).filter(title__startswith=request.POST.get('s'))
            return render(request, 'presail/prodject-presail.html',{'prod':prod, 'cont':cont , 'contac':contac, 'users':use,'compan':compan, 'comp':comp,'press':press, 'stadi':stadi , 'koment':koment ,'idollcontacts':'ollcontactsrename'})

        elif tip == 'team':
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
                        pr.projects = PresProjNew.objects.get(id =dpds[o].split('?')[0])
                        pr.cotrud = Cotrudniri.objects.get(index=dpds[o].split('?')[1])
                        pr.otch = gor
                        pr.title = i
                        #if Itap.objects.filter(projects__id=dpds[o].split('?')[0]).exclude(act='Подписан').first() == None:
                        #    pr.itap = Itap.objects.filter(projects__id=dpds[o].split('?')[0]).last()
                        #else:
                        #    pr.itap = Itap.objects.filter(projects__id=dpds[o].split('?')[0]).exclude(act='Подписан').first() 
                        pr.save()
                        o =o+1 

        return redirect("/preseil/%s/" % (pk)) 
    return render(request, 'presail/prodject-presail.html',{'prod':prod, 'komadamodel':komadamodel, 'cont':cont , 'contac':contac, 'users':use,'compan':compan, 'comp':comp,'press':press, 'stadi':stadi , 'koment':koment})

@login_required(login_url='/lg/')
def presailotchet(request):
    fio = list(PresProjNew.objects.values_list('rpproecta', flat=True).distinct())
    print(fio)
    prod = ProductProd.objects.all()
    press = PresProjNew.objects.exclude(status='Отказ').exclude(status='Завершен')
    return render(request, 'presail/prodject-presail-otch.html',{'fio':fio , 'prod':prod ,'press':press})








