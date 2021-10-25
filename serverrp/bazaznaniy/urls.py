from django.urls import path , include
from .views import main_page  , page_categoriy , page_all


app_name='bazaznaniy'

urlpatterns = [
    path('', main_page , name='main'), 
    path('cat/<str:pk>', page_categoriy , name='categori'), 
    path( 'a/', page_all , name= "catall"),
]