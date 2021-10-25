from django.urls import path

from resorsplaning.views import(
    my_prodjects_plan , otdel_prodjects_plan
)
app_name='resorsplaning'

urlpatterns = [
    path('plan', my_prodjects_plan, name='plani'),
    path('plan/<int:pk>/', otdel_prodjects_plan, name='otdel'),
    ]