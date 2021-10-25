from django import template
from django.template.defaultfilters import stringfilter
from preseil.models import StadiiProdaj  , PresailProjects , KomentForPresail , PresProjNew
from django.db.models import Q
import datetime 
#xfrom datetime import datetime
from post.models import NomerForPismo
# docdhey zadathachec
register = template.Library()

@register.filter(name='nomerpisem')
def nomerpisem(value,agr):
    try:
        return NomerForPismo.objects.filter(title=agr)
    except :
        return None


@register.simple_tag
def myznathenie(a):
    dem = {'В работе':"<span class='label label-warning'> В работе </span>", }
    try:
        
        return dem[a]
    except:
        return '-'
    


@register.filter(name='znathenie')
def znathenie(value):
    dem = {'В работе':"<span class='label label-warning'> В работе </span>", }
    try:
        
        return dem[value]
    except:
        return '-'


@register.filter(name='proxxx')
def proxxx(value):
    try:
        stadi = StadiiProdaj.objects.get(priailnnew__id = value)
        dem = [stadi.znacomstvostatus , stadi.pismostatus ,stadi.vstrethastatus ,stadi.napravleniastatus ,
            stadi.kartadorogstatus , stadi.obsledstatus , stadi.orgvoprosstatus , stadi.interviustatus ,
            stadi.otchetstatus ,stadi.zachitaotchstatus ,stadi.formirovaniepredstatus  ,
            stadi.predlojeniestatus ,stadi.soglosovaniezactatus , stadi.soglosovaniezacstatus ,
            stadi.obratnazsvazstatus  , stadi.predlojeniestatusitog  ,stadi.konkyrsnazdocstatus  ,stadi.konkursstatus
            ]
        f = 0
        for i in dem:
            if i == "Выполенно":
                f = f+1
            else:
                pass

        return round(f/18*100)
    except :
        return '-'
    


@register.filter(name='tekushiyitap')
def tekushiyitap(value):
    try:
        stadi = StadiiProdaj.objects.get(id = value)
        if stadi.kartadorogstatus != "Выполено":
            return "1 Знакомство"
        elif stadi.formirovaniepredstatus != "Выполено" :
            return "2 Экспресс-обсследование"
        elif stadi.predlojeniestatusitog != "Выполено" :
            return "3 Согласование КП"
        elif stadi.konkyrsnazdocstatus != "Выполенно" :
            return "4 Подготовка документации"
        elif stadi.konkursstatus != "Выполено" :
            return "5 Конкурсные процедуры"
        else:
            return 'Работы завершены'
    except :
        return "-"
   

@register.filter(name='active')
def active(value, agr):
    try:
        if agr == 'A':
            f =[]
            for i in list(value):
                f.append(PresProjNew.objects.filter(rpproecta=i).filter(status='Активный').count())
            return f
        elif agr == 'B':
            f =[]
            for i in list(value):
                f.append(PresProjNew.objects.filter(rpproecta=i).filter(status='На паузе').count())
            return f
    except:
    
        return [1,1]
    

@register.filter(name='statusof')
def statusof(value, agr):
    try:
        if agr == 'A':
            return PresProjNew.objects.filter(status='Активный').exclude(status="Отказ").exclude(status='Завершен').count()
        elif agr == 'B':
            return PresProjNew.objects.filter(status='На паузе').exclude(status="Отказ").exclude(status='Завершен').count()
    except :
        return 0


@register.filter(name='privleth')
def privleth(value):
    try:
        f = ''
        kanal = PresProjNew.objects.values_list('kanal', flat=True).distinct()
        print(kanal)
        for i in list(kanal):
            
            f = f + "{label: '%s' , value: %s }," %( i , PresProjNew.objects.exclude(status="Отказ").exclude(status='Завершен').filter(kanal=i).count())
        return f[:-1]
    except:
        return None
      
@register.filter(name='colof')
def colof(value, agr):
    try:
        if agr == "A":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").exclude(kartadorogstatus='Выполено').exclude(formirovaniepredstatus='Выполено').exclude(predlojeniestatusitog='Выполено').exclude(konkyrsnazdocstatus='Выполено').exclude(konkursstatus='Выполено').count()
        elif agr == "B":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").filter(kartadorogstatus='Выполено').exclude(formirovaniepredstatus='Выполено').exclude(predlojeniestatusitog='Выполено').exclude(konkyrsnazdocstatus='Выполено').exclude(konkursstatus='Выполено').count()
        elif agr == "C":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").filter(kartadorogstatus='Выполено').filter(formirovaniepredstatus='Выполено').exclude(predlojeniestatusitog='Выполено').exclude(konkyrsnazdocstatus='Выполено').exclude(konkursstatus='Выполено').count()
        elif agr == "D":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").filter(kartadorogstatus='Выполено').filter(formirovaniepredstatus='Выполено').filter(predlojeniestatusitog='Выполено').exclude(konkyrsnazdocstatus='Выполено').exclude(konkursstatus='Выполено').count()
        elif agr == "E":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").filter(kartadorogstatus='Выполено').filter(formirovaniepredstatus='Выполено').filter(predlojeniestatusitog='Выполено').filter(konkyrsnazdocstatus='Выполено').exclude(konkursstatus='Выполено').count()
        elif agr == "J":
            return StadiiProdaj.objects.exclude(priailnnew__status="Отказ").count()
    except:
        return ''
    

@register.filter(name='product')
def product(value):
    try:
        return PresProjNew.objects.exclude(status="Отказ").exclude(status='Завершен').filter(products__title=value).count()
    except:
        return 0
    
@register.filter(name='otchetpres')
def otchetpres(value):
    try:
        kom = KomentForPresail.objects.filter(priailnnew__id=value).last() 
        return kom.koment
    except :
        return ''

@register.filter(name='otchetpresdata')
def otchetpresdata(value):
    try:
        kom = KomentForPresail.objects.filter(priailnnew__id=value).last() 
        return kom.modified
    except :
        return ''


@register.filter(name='nameofcomp')
def nameofcomp(value):
    try:
        comp = {'KG':'Корпорация Галактика','AGZ':'АО Галактика Центр','IG':'АО ИТЦ Галактика','OGZ':'ООО Галактика Центр ','GP':'АО Галактика Про '}
        return comp[value]
    except :
        return ''


@register.filter(name='prefnom')
def prefnom(value):
    try:
        comp = {'KG':'00-07/','AGZ':'00-07/','IG':'10-01/','OGZ':'00-07/','GP':'10-03/'}
        return comp[value]
    except :
        return ''

