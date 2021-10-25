from django import template
from django.template.defaultfilters import stringfilter
from resurses.models import Cotrudniri , PriseofmyWok , OtchetforMonf , Zadatha , Otdel
from projects.models import Projects 
import datetime 
#xfrom datetime import datetime

from preseil.models import PresailProjects , PresProjNew
from resorsplaning.models import PlanForMyWok , OtMonf
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
def finelres(a, b ):
    try:
        return sum([ int(f.title) for f in PlanForMyWok.objects.filter(cotrud__index=a).filter(otch__id=b)])
    except:
        return '-'










