
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search_product,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('product/<str:pk>/',views.productDetails,name='productdetails'),
    path('cart/<str:pk>/',views.cart,name='cart'),
    path('cart/',views.cartdeatil,name='cartdetail'),
    path('remove/<str:pk>/',views.removeCart,name='removecart'),
   
]