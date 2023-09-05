from django.urls import path
from adminapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('addcategorypage/',views.addcategorypage,name='addcategorypage'),
    path('savecategory/',views.savecategory,name='savecategory'),
    path('displaycategory/',views.displaycategory,name='displaycategory'),
    path('editcategory/<int:dataid>/',views.editcategory,name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:dataid>/',views.deletecategory,name='deletecategory'),
    path('addproductpage/',views.addproductpage,name='addproductpage'),
    path('saveproduct/',views.saveproduct,name='saveproduct'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('displaybooking/',views.displaybooking,name='displaybooking'),
    path('deletebooking/<int:dataid>/',views.deletebooking,name='deletebooking'),
]