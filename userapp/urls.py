from django.urls import path
from userapp import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('food/<prod>/',views.food,name='food'),
    path('singlefoodpage/<int:dataid>/',views.singlefoodpage,name='singlefoodpage'),
    path('booking/',views.booking,name='booking'),
    path('aboutpage/',views.aboutpage,name='aboutpage'),
    path('savebooking/',views.savebooking,name='savebooking'),
    path('userloginpage/',views.userloginpage,name='userloginpage'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logout/',views.logout,name='logout'),
    path('cart/',views.cart,name='cart'),
]