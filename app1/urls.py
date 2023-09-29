
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search_product,name='search')
   
]