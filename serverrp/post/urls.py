from django.urls import path , include
from post.views import post_page ,post_page_generate , post_page_name , post_dowlend


app_name='post'

urlpatterns = [
    path('', post_page, name='postpage'), 
    path('<str:pk>/', post_page_generate, name='postpagegenerate'), 
    path('name/<str:pk>/', post_page_name, name='postname'), 
    path('file/<str:pk>/', post_dowlend, name='pismofile'), 
]