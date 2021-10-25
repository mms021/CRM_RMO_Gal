from django import template
from django.template.defaultfilters import stringfilter

from django.db.models import Q
from resurses.models import Otdel ,Zadatha , Contacts ,Cotrudniri , Compani , PriseofmyWok ,OtchetforMonf 
from projects.models import Projects , Itap , Komanda , Zadania , Dopsog ,Cost
import datetime 
#xfrom datetime import datetime

# docdhey zadathachec Задолжность
register = template.Library()

@register.filter(name='projfolter')
def projfolter(value, agr):
    if agr == 'sis':
        return value.filter(activedog= "Системный")
    elif agr == 'zaz':
        return value.filter(activedog= "Завершен")
    else:
        return value.exclude(activedog= "Завершен" ).exclude(activedog= "Системный")

@register.filter(name='itcount')
def itcount(value):
    it = Itap.objects.filter(projects__id=value).exclude(Q(act='Подписан',oplata= "Оплачен") & Q(komentrp="" ,komentstep=""))
    return len(it)

@register.filter(name='itapfiltersfor')
def itapfiltersfor(value, agr):
    return  Itap.objects.filter(projects__id=agr).exclude(Q(act='Подписан',oplata= "Оплачен") & Q(komentrp="" ,komentstep="") )



@register.filter(name='odshdolg')
def odshdolg(value):
    itap = Itap.objects.filter(oplata="Задолженность")
    d = 0
    for i in itap:
        try:
            
            d = d + float(i.zadolkjnost)
        except :
            pass
    return d


@register.filter(name='dolgi')
def dolgi(value):
    itap = Itap.objects.filter(oplata="Задолженность")
    return itap




@register.filter(name='itapzadolg')
def itapzadolg(value, agr):

    itap = Itap.objects.filter(projects__id=agr).filter(oplata="Задолженность")
    return itap

@register.simple_tag
def my_tag(a, b, c):
    try:
        pr = PriseofmyWok.objects.filter(cotrud__index=a).filter(otch__id=b).filter(projects__id=c).get()
        return pr.title
    except:
        return '-'
    


@register.filter(name='Naimenovanie')
def Naimenovanie(value):
    ot  = OtchetforMonf.objects.get(id=value)
    return ot.title

def datamin(a,b):
    a = a.split('-')
    b = b.split('-')
    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
    cc =bb-aa
    if str(cc)  == '0:00:00':
        return str('1 ')
    else:
        return str(cc)

@register.filter(name='lastupdete')
def lastupdete(value):
    return Itap.objects.filter(projects__id=value).first().modified

@register.filter(name='lastupdetedata')
def lastupdetedata(value):
    now = datetime.date.today()
    d = str(Itap.objects.filter(projects__id=value).first().modified)
    dat = datamin(str(now ), d.split(' ')[0])
    return  dat

def get_all_days(a, dod):
    # PV
    deay = []
    deayleft =[]
    # EV
    evday = []
    evdayleft = []
    now = datetime.date.today()
    proj = Projects.objects.get(id=a)
    itap = Itap.objects.filter(projects__title=proj.title)
    
    for i in itap:
        zadan = Zadania.objects.filter(itap__id=i.id)
        for fod in zadan:
            b = str(fod.dataend)
            b = b.split('-')
            deadline = datetime.date(int(b[0]),int(b[1]),int(b[2]))
            
            # PV ? 
            if now >= deadline:
                dadde = datamin(str(fod.data),str(fod.dataend))
                deay.append(int(dadde.split()[0]))
            else:
                dadde = datamin(str(fod.data),str(fod.dataend))
                deayleft.append(int(dadde.split()[0]))

            # EV Стоимость выполенненных работ 
            if  fod.prozes == '100%':
                dadde = datamin(str(fod.data),str(fod.dataend))
                #pr = int(fod.prozes[:-1])/100
                evday.append(int(dadde.split()[0]) )
            else:
                dadde = datamin(str(fod.data),str(fod.dataend))
                evdayleft.append(int(dadde.split()[0]))

            """
            if  fod.prozes != '0%':
                dadde = datamin(str(fod.data),str(fod.dataend))
                pr = int(fod.prozes[:-1])/100
                evday.append(int(dadde.split()[0]) *pr )
            else:
                dadde = datamin(str(fod.data),str(fod.dataend))
                evdayleft.append(int(dadde.split()[0]))
            """

    
    if dod == "EV":
        a = sum(evday) 
        xc = sum(evdayleft) 
        return [a, xc]
    elif  dod == "PV":
        a = sum(deay) 
        xc = sum(deayleft) 
        return [a, xc]
    elif  dod == "SV":
        a = sum(evday) 
        xc = sum(evdayleft) 
        a1 = sum(deay) 
        xc1 = sum(deayleft) 
        return [a, xc ,a1,xc1]
    else:
        pass


@register.filter(name='DAT')
def DAT(value , agr):

    proj = Projects.objects.get(id=value)
    try:
        # 
        if agr == "EV":
            d = get_all_days(value,agr)
            dya = int(d[0]) + int(d[1])
            foer = int(proj.prisepr)/dya*int(d[0])
            return round(foer,2)
        #
        elif agr == "PV":
            d = get_all_days(value,agr)
            dya = int(d[0]) + int(d[1])
            foer = int(proj.prisepr)/dya*int(d[0])
            return round(foer,2)
        #
        elif agr == "CV":
            d = get_all_days(value,'EV')
            dya = int(d[0]) + int(d[1])
            foer = int(proj.prisepr)/dya*int(d[0])
            cost = Cost.objects.filter(projects__title=proj.title)
            co = []
            for i in cost:
                co.append(int(i.serios))
            how = sum(co)
            foer = foer - how
            return round(foer,2)
        #
        elif agr == "SV":
            d = get_all_days(value,agr)
            dya = int(d[0]) + int(d[1])
            ev = int(proj.prisepr)/dya*int(d[0])
            dya = int(d[2]) + int(d[3])
            pv = int(proj.prisepr)/dya*int(d[2])
            return round(ev - pv,2)
        #
        elif agr == "SPI":
            d = get_all_days(value,'SV')
            dya = int(d[0]) + int(d[1])
            ev = int(proj.prisepr)/dya*int(d[0])
            dya = int(d[2]) + int(d[3])
            pv = int(proj.prisepr)/dya*int(d[2])
            return round(ev / pv,2)
        #
        elif agr == "TCPI":
            d = get_all_days(value,'SV')
            dya = int(d[0]) + int(d[1])
            ev = int(proj.prisepr)/dya*int(d[0])
            dya = int(d[2]) + int(d[3])
            pv = int(proj.prisepr)/dya*int(d[2])
            tcpi = (int(proj.prisepr) - ev) /(int(proj.prisepr) - pv)
            return round(tcpi,2)
        #    
        elif agr == "ETC":
            d = get_all_days(value,'EV')
            dya = int(d[0]) + int(d[1])
            ev = int(proj.prisepr)/dya*int(d[0])
            cost = Cost.objects.filter(projects__title=proj.title)
            co = []
            for i in cost:
                co.append(int(i.serios))
            ac = sum(co)
            cpi =(ev / ac) 
            eac = int(proj.prisepr)/cpi 
            return round(eac - ac,2)  
        else:
            return '-'
    except:
        return '-'


def get_all_summ(a, dod):
    evday = []
    pvday = []
    now = datetime.date.today()
    proj = Projects.objects.get(id=a)
    itap = Itap.objects.filter(projects__title=proj.title)
    lev = []

    for i in itap:
        zadan = Zadania.objects.filter(itap__id=i.id)
        for fod in zadan:
            b = str(fod.dataend)
            b = b.split('-')
            deadline = datetime.date(int(b[0]),int(b[1]),int(b[2]))
            b1 = str(fod.data)
            b1 = b1.split('-')
            deadline1 = datetime.date(int(b1[0]),int(b1[1]),int(b1[2]))
            x = fod.level.split('.')
            lev.append(len(x))

            # PV ?            
            if len(x) == lev[0] and  now >= deadline:
                summ = fod.rezult 
                pvday.append(int(summ.replace(' ','')))
            elif len(x) == lev[0] and now >= deadline1 and now <= deadline:
                dadde = datamin(str(fod.data),str(fod.dataend))
                summ = fod.rezult 
                pvday.append(int(summ.replace(' ','')) / int(dadde.split()[0]))
            else:
                pass
            
            # EV Стоимость выполенненных работ 
            if  fod.prozes == '100%' and len(x) == lev[0]:
                summ = fod.rezult 
                evday.append(int(summ.replace(' ','')))
            else:
                pass

    a = sum(evday) 
    f = sum(pvday) 

    if dod == "EV":
        return a
    elif  dod == "PV":
        return f
    elif  dod == "SV":
        return [a , f]
    else:
        pass


@register.filter(name='DATT')
def DATT(value , agr):
    proj = Projects.objects.get(id=value)
    try:
        
        # EV
        if agr == "EV":
            d = get_all_summ(value,agr)
            return round(d,2)
        # PV
        elif agr == "PV":
            d = get_all_summ(value,agr)
            return round(d,2)
        #PC
        elif agr == "PC":
            prise = int(proj.prisezatrat)
            d = get_all_summ(value,"EV")
            return round(d / prise * 100  )
        # CV    
        elif agr == "CV":
            d = get_all_summ(value,'EV')
            prise = int(proj.prisezatrat)
            cost = Cost.objects.filter(projects__title=proj.title)
            co = []
            for i in cost:
                co.append(int(i.serios))
            ac = sum(co)
            foer = d - ac
            return round(foer,2)
        # SV
        elif agr == "SV":
            d = get_all_summ(value,agr)
            return round(d[0] - d[1] ,2)
        # SPI
        elif agr == "SPI":
            d = get_all_summ(value,'SV')
            return round(d[0] / d[1],2)
        # TCPI
        elif agr == "TCPI":
            d = get_all_summ(value,'EV')
            prise = int(proj.prisezatrat)
            cost = Cost.objects.filter(projects__title=proj.title)
            co = []
            for i in cost:
                co.append(int(i.serios))
            ac = sum(co)
            tcpi = (prise - d) /(prise - ac)
            return round(tcpi,2)
        # ETC   
        elif agr == "ETC":
            ev = get_all_summ (value,'EV')
            prise = int(proj.prisezatrat)
            cost = Cost.objects.filter(projects__title=proj.title)
            co = []
            for i in cost:
                co.append(int(i.serios))
            ac = sum(co)
            cpi =(ev / ac) 
            eac = prise/cpi 
            return round(eac - ac,2)  
        else:
            return '-'
    except:
        return '-'


@register.filter(name='PROZ')
def PROZ(value , agr):
    try:
        now = datetime.date.today()
        if agr == 'ITAP':
            itap = Itap.objects.get(id=value)
            
            try:
                deay = []
                deayleft = []
                lev =[]
                zadan = Zadania.objects.filter(itap__id=itap.id)
                for fod in zadan:
                    b = str(fod.dataend)
                    b = b.split('-')
                    deadline = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    
                    # PV ? 
                    x = fod.level.split('.')
                    lev.append(len(x))
                    if len(x) == lev[0] and  now >= deadline:
                    
                        dadde = datamin(str(fod.data),str(fod.dataend))
                        deay.append(int(dadde.split()[0]))
                    elif len(x) == lev[0]:
                        dadde = datamin(str(fod.data),str(fod.dataend))
                        deayleft.append(int(dadde.split()[0]))
 
                    else:
                         pass
                a = sum(deay) 
                xc = sum(deayleft) 
                deh = abs(a) * 100
                fr = a+ xc
                deh = deh / fr
                return str(round(deh))+'%'

            except:
                # Дней в Этапе
                dat = datamin(str(itap.datastart),str(itap.datastop))
                # Дней прошло
                dat2 = datamin(str(itap.datastart),str(now))
                # Дней между 1 и 2 датами 
                deh = abs(int(dat2.split()[0])) * 100
                q = deh / int(dat.split()[0])


                if now < itap.datastart:
                    return "0%"
                elif now > itap.datastop:
                    return "100%"
                else:
                    return str(round(q))+'%'
                    

        elif agr == "ZADATHA":
            pass
        elif agr == "PROECT":
            proj = Projects.objects.get(id=value)
            try:
                itap = Itap.objects.filter(projects__title=proj)
                deay = []
                deayleft = []
                lev = []
                
                for i in itap:
                    zadan = Zadania.objects.filter(itap__id=i.id)
                    for fod in zadan:
                        b = str(fod.dataend)
                        b = b.split('-')
                        deadline = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                        x = fod.level.split('.')
                        lev.append(len(x))
                        # PV ? 
                        if len(x) == lev[0] and  now >= deadline:
                            dadde = datamin(str(fod.data),str(fod.dataend))
                            deay.append(int(dadde.split()[0]))
                        elif len(x) == lev[0] :
                            dadde = datamin(str(fod.data),str(fod.dataend))
                            deayleft.append(int(dadde.split()[0]))
                        else:
                            pass

                a = sum(deay) 
                xc = sum(deayleft) 
                deh = abs(a) * 100
                fr = a+ xc
                deh = deh / fr
                return str(round(deh))+'%'

            except:
                itap = Itap.objects.filter(projects__title=proj).first()
                itap1 = Itap.objects.filter(projects__title=proj).last()
                dat = datamin(str(itap.datastart),str(itap1.datastop))
                # Дней прошло
                dat2 = datamin(str(itap.datastart),str(now))
                deh = abs(int(dat2.split()[0])) * 100
                q = deh / int(dat.split()[0])

                if now < itap.datastart:
                    return "0%"
                elif now > itap1.datastop:
                    return "100%"
                else:
                    return str(round(q))+'%'
        else:
            return '-'
    except:
        return '-'

@register.filter(name='itcou')
def itcou(value):
    it = Itap.objects.filter(projects__id = value)
    return len(it)

@register.filter(name='it')
def it(value, arg):
    it = Itap.objects.filter(projects__id = arg)
    return it

# Дата начала 
@register.filter(name='datastartitm')
def datastartitm(value):
    try:
        proj = Projects.objects.get(id=value)
        itap = Itap.objects.filter(projects__title=proj).first()
        return itap.datastart
    except:
        return "-"

# ДАта Конца 
@register.filter(name='datastopitm')
def datastopitm(value):
    try:
        proj = Projects.objects.get(id=value)
        itap = Itap.objects.filter(projects__title=proj).last()
        return itap.datastop
    except:
        return "-"

@register.filter(name='LEVL')
def LEVL(value):
    zadan = Zadania.objects.get(id = value)
    zad = Zadania.objects.filter(id__gt=value).filter(itap__id=zadan.itap.id)
    le = str(zadan.level)
    #f = len(le.split('.'))
    #x = []
    for i in zad:
        #print(len(i.level.split('.')), f)
        #print(le.split('.'),i.level.split('.') )
        if len(i.level.split('.')) <= len(le.split('.')):
            return '2'
            
        else:
            #print(i.id)
            return '1'
            
    
@register.filter(name='LEVLdat')
def LEVLdat(value):
    try:
        zadan = Zadania.objects.get(id = value)
        zad = Zadania.objects.filter(id__gt=value).filter(itap__id=zadan.itap.id)
        
        re =[]
        d = 0
        for i in zad:
            
            if len(zadan.level.split('.')) < len(i.level.split('.')):
                # print(i.id, i.level ,zadan.level )
                re.append(int(i.prozes[:-1]))
                d = d +1
            else:
                pass

        re = sum(re)/d
        #print(re,d)
        zadan.prozes = str(round(re))+'%'
        zadan.save()
        return str(round(re))+'%'
    except:
        return '-'  
    

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')


@register.filter(name='hi')
def hi(value):
    itap = Itap.objects.get(id=value)
    try:
        a = str(itap.datastart)
        b = str(itap.datastop)
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        cc =bb-aa
        dd = str(cc)
        # сверху разница между днями снизу разница между первм и текущим 
        bb1 = datetime.date.today()
        cc1 = bb1 - aa  
        dd11 = str(cc1)
        dd1 = int(dd11.split()[0]) if int(dd11.split()[0]) > 0 else -int(dd11.split()[0])
        q1 = int(dd1) * 100
        q = q1 / int(dd.split()[0])
        #print(q)
        #print(dd.split()[0], dd1.split()[0])
        if dd11[0] == "-":
            return "0%"
        else:
            if q >= 0 and q <= 100:
                return str(round(q))+'%'
            elif q >= 100:
                return "100%"
            elif q <= 0:
                return "0%"
    except:
        return "-"




@register.filter(name='prozent')
def prozent(value):
    itap = Itap.objects.get(id=value)
    #zadan = Zadania.objects.filter(id=value)
    zadan = Zadania.objects.filter(itap__id=itap.id)
    levl = []
    d = 0
    re = [ ]
    try:
        for ier in zadan:
            le = ier.level
            le.split('.')
            if len(levl) == 0:
                re.append(int(ier.prozes[:-1]))
                levl.append(len(le))
                d = d+1
            elif len(le) == levl[0]:
                re.append(int(ier.prozes[:-1]))
                d = d+1
            else:
                pass
 
        pov  = sum(re)
        ae = pov/d
        return round(ae)
    except:
        return "-"


@register.filter(name='dneymezdu')
def dneymezdu(value):
    zadan = Zadania.objects.get(id=value)

    try:
        a = str(zadan.data)
        b = str(zadan.dataend)
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        cc =bb-aa
        ddd = str(cc)

        q = ddd.split()[0]

        if q >= 0 and q <= 100:
            return str(round(q))+'%'
        elif q >= 100:
            return "100%"
        elif q <= 0:
            return "0%"
    except:
        return "-"




@register.filter(name='docdhey')
def docdhey(value):
    itap = Zadania.objects.get(id=value)
    try:
        a = str(itap.data)
        b = str(itap.dataend)
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        cc =bb-aa
        dd = str(cc)
        
        bb1 = datetime.date.today()
        cc1 = bb1 - aa  
        dd11 = str(cc1)
        dd1 = int(dd11.split()[0]) if int(dd11.split()[0]) > 0 else -int(dd11.split()[0])
        q1 = int(dd1) * 100
        q = q1 / int(dd.split()[0])
        if dd11[0] != '-':
            if q >= 0 and q <= 100:
                return str(round(q))+'%'
            elif q >= 100:
                return "100%"
            elif q <= 0:
                return "0%"
        else:
            return "0%"
    except:
        return "-"



@register.filter(name='prozentpo')
def prozentpo(value):
    #proj = Projects.objects.get(id=value)
    itap = Itap.objects.filter(projects__title=Projects.objects.get(id=value))
    #zadan = Zadania.objects.filter(id=value)
    lev= []
    gog = []
    nom = 0
    try:
        for i in itap:
            zadan = Zadania.objects.filter(itap__id=i.id)
            for gov in zadan:
                x = gov.level.split('.')
                lev.append(len(x))
                if len(x) == lev[0]:
                    gog.append(int(gov.prozes[:-1]))
                    nom = nom+1
                elif len(x) == lev[0]:
                    nom = nom+1
                else:
                    pass

        pov  = sum(gog)
        ae = pov/nom

        return round(ae)
    except:
        return "-"



    
@register.filter(name='prozentplan')
def prozentplan(value):
    #proj = Projects.objects.get(id=value)
    itap = Itap.objects.filter(projects__title=Projects.objects.get(id=value))
    #zadan = Zadania.objects.filter(id=value)
    gog = []
    
    try:
        for i in itap:
            gog.append(i.datastart)
            gog.append(i.datastop)

        a = str(gog[0])
        b = str(gog[-1])
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        cc =bb-aa
        dd = str(cc)
        
        bb1 = datetime.date.today()
        cc1 = bb1 - aa  
        dd11 = str(cc1)
        dd1 = int(dd11.split()[0]) if int(dd11.split()[0]) > 0 else -int(dd11.split()[0])
        q1 = int(dd1) * 100
        q = q1 / int(dd.split()[0])

        if q >= 0 and q <= 100:
            return str(round(q))
        elif q >= 100:
            return "100"
        elif q <= 0:
            return "0"
    except:
        return "-"

#zadathachec   
@register.filter(name='priseday')
def priseday(value):
    proj = Projects.objects.get(id=value)
    itap = Itap.objects.filter(projects__title=proj.title)

    de = []
    day =[]
    try:
        for i in itap:
            zadan = Zadania.objects.filter(itap__id=i.id)
            for fod in zadan:
                #print(fod.level)
                if len(de) == 0:
                    a = str(fod.data)
                    b = str(fod.dataend)
                    
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    
                    #print('1')
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(int(1))
                        
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))
                        

                elif len(de[-1]) >= len(fod.level):
                    a = str(fod.data)
                    b = str(fod.dataend)
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    #print('2')
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(int(1))
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))
                elif len(de[-1]) < len(fod.level):
                    
                    day.pop()
                    day.append(int(0))
                    a = str(fod.data)
                    b = str(fod.dataend)
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    #print('3')
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(1)
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))

                else:
                    print('err')

        mao = int(proj.prisepr)
        pov  = sum(day)        
        foer = mao/pov    
        return  round(foer)
    except:
        return "-"
        

    
@register.filter(name='plandeneg')
def plandeneg(value):


    proj = Projects.objects.get(id=value)
    itap = Itap.objects.filter(projects__title=proj.title)
    
    de = []
    day =[]
    dya = []
    try:
        for i in itap:
            zadan = Zadania.objects.filter(itap__id=i.id)
            dya.append(i.datastart)
            dya.append(i.datastop)
            for fod in zadan:
                #print(fod.level)
                if len(de) == 0:
                    a = str(fod.data)
                    b = str(fod.dataend)
                    
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    
                    #print('1
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(int(1))
                               
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))
                               

                elif len(de[-1]) >= len(fod.level):
                    a = str(fod.data)
                    b = str(fod.dataend)
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    #print('2')
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(int(1))
                               
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))
                                 

                elif len(de[-1]) < len(fod.level):
                    
                    day.pop()
                    day.append(int(0))
                    a = str(fod.data)
                    b = str(fod.dataend)
                    a = a.split('-')
                    b = b.split('-')
                    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
                    cc =bb-aa
                    dd = str(cc)
                    #print('3')
                    
                    if dd  == '0:00:00':
                        de.append(fod.level)
                        day.append(int(1))
                              
                    else:
                        de.append(fod.level)
                        day.append(int(dd.split()[0]))    
                else:
                    print('err')
        
        
        a =str(dya[0])
        #b =str(dya[-1])
        a = a.split('-')
        #b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        #bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        #cc = bb - aa

        bb1 = datetime.date.today()
        cc1 = bb1 - aa  
        dd11 = str(cc1)
        mao = int(proj.prisepr)

        
        pov  = sum(day)        
        foer = mao/pov*int(dd11.split()[0]) 
        if foer < mao:   
            return  round(foer)
        else:
            return "потраченно "
    except:
        return "-"



   
@register.filter(name='zadathachec')
def zadathachec(value):
    proj = Projects.objects.get(id=value)
    itap = Itap.objects.filter(projects__title=proj.title)
    #zad= []
    de = 0
    day =[]
    dya = []
    #dood = []
    proz = []
    day1 =[]
    try:
        for i in itap:
            zadan = Zadania.objects.filter(itap__id=i.id)
            #ros = datamin(str(i.datastart),str(i.datastop))
            #dya.append(int(ros.split()[0]))
            for fod in zadan:
                if de == 0:
                    dd = datamin(str(fod.data),str(fod.dataend))
                    de = len(fod.level)
                    day.append(int(dd.split()[0]))
                    proz.append(fod.prozes)
                    
                elif de == len(fod.level):          
                    dd = datamin(str(fod.data),str(fod.dataend))
                    day.append(int(dd.split()[0]))
                    proz.append(fod.prozes)
                    
                else:
                    dd = datamin(str(fod.data),str(fod.dataend))
                    day1.append(int(dd.split()[0]))
                    
        q = [] 
        
        ert = 0
        for ient in day:
            if proz[ert] =='100%':
                q.append(int(ient))
                ert =ert+1
            else:
                ert =ert+1

        #print(dya, day ,proz)
        mao = int(proj.prisepr)
        der = sum(q)
        dya = dya + day1
        pov  = sum(dya)       
        #print(der,pov)
        foer = mao/pov*der

        #proj.osvoeno = str(round(foer))
        #proj.save()

        if foer < mao:   
            return  round(foer)
        else:
            return "потраченно "
    except:
        return "-"
#docdhey

@register.filter(name='costzatrat')
def costzatrat(value):   
    proj = Projects.objects.get(id=value)
    cost = Cost.objects.filter(projects__title=proj.title)

    try:
        co = []
        for i in cost:
            co.append(int(i.serios))
        how = sum(co)
        return how
    except:
        return "-"


@register.filter(name='BAC')
def BAC(value):
    try:
        #proj = Projects.objects.get(id=value)


        return "-1"
    except: 
        return "-"



    

# Доработать - Убрать подэтапы и разобраться с паралельными задачами 
# Умножить на цену дня 
@register.filter(name='EV')
def EV(value):    
    try:
        dop = []
        dpo2 =[]
        #now = datetime.date.today()
        proj = Projects.objects.get(id=value)
        itap = Itap.objects.filter(projects__title=proj.title)
        
        for i in itap:
            zadan = Zadania.objects.filter(itap__id=i.id)
            for fod in zadan:
                if  fod.prozes == '100%':
                    dadde = datamin(str(fod.data),str(fod.dataend))
                    dop.append(int(dadde.split()[0]))
                else:
                    dadde = datamin(str(fod.data),str(fod.dataend))
                    dpo2.append(int(dadde.split()[0]))
                    
                    
        dpo2 = dpo2 + dop
        mao = int(proj.prisepr) /sum(dpo2)


        return round(sum(dop)*mao,2)
    except: 
        return "-"



    


    
