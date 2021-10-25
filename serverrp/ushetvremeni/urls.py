from django.urls import path

from ushetvremeni.views import(
    my_otdel_plan 
)
app_name='ushetvremeni'

urlpatterns = [
    path('<int:pk>/', my_otdel_plan, name='vrem'),
   
    ]


