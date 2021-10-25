
from django.urls import path , include
from projects.views import(
    projects_views , projects_detail, otchet , logout_view, logins , projects_detail_st_low , list_otch ,dashboard_allprod,
    projects_views_all, dashbotrd_pass, dashboard_pasport , dashboard_myprod ,dashboard_operplan ,
    pmo_main_page ,pmo_post_page,  deshbord_prodj,  pasport_red,
    check , dashbord_pocaz , otchet_new , del_sotr_from
)

app_name='projects'

urlpatterns = [
    path('', projects_views, name='views'), # все проекты / Мои проекты (отчеты)
    path('<int:pk>/',projects_detail,name='detail'), # отче проекта
    path('otch/',otchet,name='otch'),#  отчет для М
    path('otch2/',otchet_new,name='otchetnew'),#  отчет для М 2
    path('logout/',logout_view ,name='logout'),# Выйти
    path('lg/', logins ,name='ligin'),# Войти 
    path('st/<int:pk>/', projects_detail_st_low,name='detail_st'),# Отчет проекта- Степанова
    path('ch/', check , name='chrck'),# Проверка обновления Обновить код 
    path('pmomaim/',pmo_main_page, name="pmo"),# PMO
    path('pmopost/',pmo_post_page, name="pmopost"),#  РМО paccылка
    path('allprod/' ,dashboard_allprod , name="allprod"),# Все проекты (Пас)
    path('myprod/' ,dashboard_myprod , name="myprod"),# Мои проекты (Пас)
    path('proect/<int:pk>/' ,dashboard_pasport , name="passs"),# Паспорт проекта 
    path('operplam/<int:pk>/',dashboard_operplan, name="operplan"),# Обновить говно полное  
    path('dashboard/' , deshbord_prodj , name="dashbord"),# Доработаь 
    path('ot/', list_otch ,name='list'),# Общий отчет с возможностью менять (Перписать)
    path('all/', projects_views_all , name='all'),#Все проекты  (отчеты)
    path('otshetpass/',dashbotrd_pass, name='dashpass' ), # Отчет таблица общий без сылок 
    path('pasportre/<int:pk>/',pasport_red, name="pasportre"), # редактировать информацию по проекту 

    path('del/<int:pk>/<str:cot>/', del_sotr_from , name='del_sort_form'  ), # Удалить сотрудкника 

    path('pok/<int:pk>/',dashbord_pocaz, name="pok"),# удалить нахер 
    #path('test/', projects_views2 , name='views2'),# ТеСТ
    #path('creat/',crete_prodjects, name='create'),# удалить нахер 
    #path('proect/', projects_moiproecs, name='moipr'),# Удалить не актуально
    #path('mig/', from_exel_to_sql),#удалить нахер 
    #path('pasport/<int:pk>/',dashbord_pocaz, name="pasport"),# удалить нахер 
    #path('pasport/ch/<int:pk>', pr_pasport_red, name="pasportred"),#удалить нахер 
    #path('zadatha/',zadatha, name = "zadatha" ),#удалить нахер 
    #path('zadath/<int:pk>' , zadaniadetail , name="zadditail"),#удалить нахер 
    #path('zadathamoi/',zadathamoi, name = "zadathamoi"),#удалить нахер 
    #path('zadathvse/<int:pk>' ,zadathavse , name="zadathavse"),#удалить нахер 
    #path('create/',   dashboard_create, name='creates') # Надо доделать, а лучше перенести в другой модуль 
]
