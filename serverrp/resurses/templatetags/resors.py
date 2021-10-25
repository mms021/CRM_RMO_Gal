from django import template
from django.template.defaultfilters import stringfilter
from resurses.models import Cotrudniri , PriseofmyWok , OtchetforMonf , Zadatha , Otdel
from projects.models import Projects 
import datetime 
#xfrom datetime import datetime

from preseil.models import PresailProjects , PresProjNew
#
register = template.Library()

@register.simple_tag
def checmdisable(a , b , c = None ):
    try:
        if c == None: 
            c  = OtchetforMonf.objects.last()
        else:
            c = OtchetforMonf.objects.get(id = c)
        pr = Cotrudniri.objects.filter(projects__id = a).filter(index=b).get()
        #pr = PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).get()
        if PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).exists():    
            pr = PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).get()
            if pr.soglos == 'soglos':
                return 'disabled'
        else:
            return " "
    except:
        return " "   


@register.simple_tag
def checmyresors(a , b ,  c = None  ):
    try:
        if c == None: 
            c  = OtchetforMonf.objects.last()
        else:
            c = OtchetforMonf.objects.get(id = c)

        pr = Cotrudniri.objects.filter(projects__id = a).filter(index=b).get()
        #pr = PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).get()
        if PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).exists():    
            pr = PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).get()
            return pr.title
        else:
            return "-"
    except:
        return "non"   







@register.filter(name='projcount')
def projcount(value):
    try:
        zada = Projects.objects.filter(rpproecta=value).exclude(activedog ="Системный").exclude(activedog ="Завершен").count()
        return str(zada)
    except:
        return '0'

@register.filter(name='presailcount')
def presailcount(value):
    try:
        zada = PresProjNew.objects.filter(rpproecta=value).filter( status='Активный').count()
        return str(zada)
    except:
        return '0'

@register.filter(name='otdelfilf')
def otdelfilf(value , agr):
    try:
        # Otdel.objects.filter(rpotdela='agr') Otdel.objects.all()
        return Otdel.objects.filter(rpotdela=agr) 
    except:
        return  None
    

@register.filter(name='mailbox')
def mailbox(value):
    try:
        zada = Zadatha.objects.filter(user__username=value).exclude(chec='checked').count()
        return str(zada)
    except:
        return '0'

@register.filter(name='lastupdete')
def lastupdete(value):
    return "--"

@register.filter(name='lastupdetedata')
def lastupdetedata(value):
    
    return  "--"


@register.filter(name='sotrudnik')
def sotrudnik(value , agr):
    return Cotrudniri.objects.filter(projects__id=agr).exclude(statusof='Уволен')

    
@register.filter(name='prozent')
def prozent(value , agr):
    try:
        gor  = OtchetforMonf.objects.all().last()
        pr = PriseofmyWok.objects.filter(cotrud__index=value).filter(otch=gor)
        q = []
        for i in pr:
            q.append(int(i.title))
        d = sum(q)

        return  round(int(agr)/d*100 )
    except:
        return '-'



@register.filter(name='prot')
def prot(value , agr):
    try:
        gor  = OtchetforMonf.objects.all().last()
        pr = PriseofmyWok.objects.filter(projects_id=value).filter(cotrud__index=agr).filter(otch=gor).get()
        return pr.title
    except:
        return '-'


@register.filter(name='itog')
def itog(value , agr):
    try:
        gor  = OtchetforMonf.objects.all().last()
        pr = PriseofmyWok.objects.filter(cotrud__index=agr).filter(otch=gor)
        fi =[]
        for i in pr:
            fi.append(int(i.title))
        return sum(fi)
    except:
        return '-'



@register.filter(name='prid')
def prid(value , agr ):
    try:
        gor  = OtchetforMonf.objects.all().last()
        pr = PriseofmyWok.objects.filter(cotrud__index=agr).filter(otch=gor).filter(projects__id=value).get()
        return pr.title
    except:
        return '-'


@register.filter(name='priddisable')
def priddisable(value , agr ):
    try:
        gor  = OtchetforMonf.objects.all().last()
        pr = PriseofmyWok.objects.filter(cotrud__index=agr).filter(otch=gor).filter(projects__id=value).get()
        return 'disabled'
    except:
        return ''


@register.filter(name='cotrudcompani')
def cotrudcompani(value , agr):
    return Cotrudniri.objects.filter(compan__id=agr)


@register.filter(name='notinprojdisable')
def notinprojdisable(value , agr ):
    try:
        pr = Cotrudniri.objects.filter(projects__id = agr).filter(index=value).get()
        return ''
    except:
        return 'hidden'


@register.simple_tag
def resors_of_work(a, b, c):
    try:
        pr = PriseofmyWok.objects.filter(cotrud__index=b).filter(otch=c).filter(projects_id=a).get()
        return pr.title
    except:
        return " "