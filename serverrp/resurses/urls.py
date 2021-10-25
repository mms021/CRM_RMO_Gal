from django.urls import path
from resurses.views import(
    main ,contacts , mycontacts , mycontactcreate, myplans , 
    myworkers , mywokrcrete ,myworcersall ,mywokrcrename , mcontactdetail ,allcompanis , resorsmatc_all
    ,myotdel , allresorses , resorsmatch , rezalt , otdelcontacts , companicontacts , allcontactscompani, 
    otdelcontacts_all , soglosovanie_resursu , makemigratinonresors , prog
)
app_name='resurses'

urlpatterns = [
    path('g', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('mycont/<int:pk>/' , mycontacts, name = 'myconts'),
    path('plans/', myplans , name='myplans'),
    path('mycontcr/<int:pk>/' , mycontactcreate, name ='mycontscr'),
    path('workers/<int:pk>/' , myworkers , name="myworkers" ),
    path('rename/<str:pk>/' , mywokrcrename , name="mywokrcrename" ),
    path('myworcersall/', myworcersall , name='myworcersall'),
    path('mywokrcrete/', mywokrcrete , name='mywokrcrete'),
    path('myotdel/<int:pk>/' , myotdel , name="myotdel" ),
    path('otdelcontacts/<int:pk>/' , otdelcontacts , name="otdelcontacts" ),
    path('allresorses/', allresorses , name='allresorses'),
    path('resorsmatch/', resorsmatch , name='resorsmatch'),
    path('rezalt/<int:pk>/', rezalt , name='rezalt'),
    path('companicontacts/<int:pk>/', companicontacts , name='companicontacts'),
    path('allcontactscompani/', allcontactscompani , name='allcontactscompani'),
    path('allcompanis/', allcompanis , name='allcompanis'),
    path('cont/<str:pk>/',mcontactdetail, name='contactsname'),
    path('resorsmatcofall/', resorsmatc_all , name='resorsmatcofall'),
    path('allotd/<str:pk>/',otdelcontacts_all, name='allotd'),
    path('soglos/', soglosovanie_resursu , name = 'soglosov'),
    path('mig/<str:pk>/', makemigratinonresors),
    path('d/', prog ),
]

#