
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('productdetails/<str:pk>/',views.product,name='product')
    path('home/',views.home,name='home')
   
]