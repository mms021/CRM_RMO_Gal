from django.urls import path , include
from preseil.views import (
    preseilmain , preseilmainall , preseilmainmy ,preseilnew ,presailotchet
)
app_name='preseil'

urlpatterns = [
    path('<int:pk>/', preseilmain, name='preselproj'), 
    path('', preseilmainmy, name='presailall'), 
    path('all/', preseilmainall, name='presail'), 
    path('new/', preseilnew, name='presailnew'), 
    path('otch/', presailotchet, name='presailotchet'), 
]