
from django.urls import path
from glavarp.views import(
    main_page , post_page , projectstest , docwith  ,adminmain , 
    operplans ,migratio_to_br, operplan , cotrudniki , compani , presaiall
)
app_name='glavarp'
# {% url 'glavarp:cotrudniki' %}
urlpatterns = [
    path('g', main_page, name='main'),
    path('j/',post_page, name='post'),
    path('creatrnew/',docwith, name='doc'),
    path('operplan/',operplans, name='op'),
    path('migr/',migratio_to_br, name='mig'),
    path('',adminmain, name='admins'),
    path('qff/<int:pk>/',operplan, name='oper'),
    path('cotrudniki/',cotrudniki, name='cotrudniki'),
    path('presaiall/',presaiall, name='presaiall'),
    path('compani/',compani, name='compani'),

    path('q/',projectstest, name='proj')
]
