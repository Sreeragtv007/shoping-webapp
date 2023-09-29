
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search_product,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
   
]