from django import template
from django.template.defaultfilters import stringfilter
from resurses.models import Cotrudniri , PriseofmyWok , OtchetforMonf , Zadatha , Otdel
from projects.models import Projects 

from ushetvremeni.models import UshetResursov

import datetime
import calendar
#
register = template.Library()

@register.simple_tag
def plan_resors_of_work(a, b, c):
    if Cotrudniri.objects.filter(projects__id = a).filter(index=b).exists():
        try:
            la = PlanForMyWok.objects.filter(projects__id=a).filter(cotrud__index=b).filter(otch__id=c).get()
            return {'nom': 'da' , 'tit': la.title}
        except:
            return {'nom': 'da', 'tit': '-' }
    else:
        return {'nom': 'no' }

@register.simple_tag
def dataflip( a , year , month ):
    if a[0][0] == 0  :
        l = a[-1][0]
    elif a[-1][0] == 0:
        l = l = a[0][0]
    else: 
        l = l = a[0][0]
    
    return f'{ datetime.date(year, month ,l ).isocalendar()[1] }'


@register.simple_tag
def datafilters(a, b , c):
    #print(calendar.Calendar(firstweekday=0).monthdatescalendar(a, b)[0][0])
    for i in calendar.Calendar(firstweekday=0).monthdatescalendar(a, b):
        if i[0].isocalendar()[1]  == int(c):
            return i
    

@register.filter(name='datavalue')
def datavalue(a , b ):
    return a[int(b)]


@register.simple_tag
def valuesofthe(a, b , c):
    ca = Cotrudniri.objects.get(index=c)
    obj, created = UshetResursov.objects.get_or_create(title=a , year=b, cotrud=ca )
    obj.save()
    return obj.rezalt.split(',')