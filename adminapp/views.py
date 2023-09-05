from django.shortcuts import render,redirect
from adminapp.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from userapp.models import bookingdb

# Create your views here.
def indexpage(req):
    return render(req,'index.html')
def addcategorypage(req):
    return render(req,'Addcategory.html')
def savecategory(req):
    if req.method=="POST":
        na=req.POST.get('name')
        de=req.POST.get('description')
        im=req.FILES['image']
        obj=categorydb(Category_Name=na,Description=de,Image=im)
        obj.save()
        return redirect(addcategorypage)
def displaycategory(req):
    data=categorydb.objects.all()
    return render(req,'categorydisplay.html', {'data':data})
def editcategory(req,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(req,'categoryedit.html', {'data':data})
def updatecategory(req,dataid):
    if req.method=="POST":
        na=req.POST.get('name')
        de=req.POST.get('description')
        try:
            im = req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Category_Name=na,Description=de,Image=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data=categorydb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)


def addproductpage(req):
    category=categorydb.objects.all()
    return render(req,'Addproduct.html',{'category':category})
def saveproduct(req):
    if req.method=="POST":
        ca=req.POST.get('category')
        na=req.POST.get('name')
        de=req.POST.get('description')
        pr=req.POST.get('price')
        im=req.FILES['image']
        obj=productdb(Category_Name=ca,Description=de,Image=im,Price=pr,Name=na)
        obj.save()
        return redirect(addproductpage)
def displayproduct(req):
    data=productdb.objects.all()
    return render(req,'productdisplay.html', {'data':data})
def editproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    category=categorydb.objects.all()
    return render(req,'editproduct.html', {'data':data, 'category':category})
def updateproduct(req,dataid):
    if req.method=="POST":
        ca=req.POST.get('category')
        na=req.POST.get('name')
        de=req.POST.get('description')
        pr=req.POST.get('price')
        try:
            im=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Category_Name=ca,Description=de,Image=file,Price=pr,Name=na)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    data.delete()
    return redirect(displayproduct)
def displaybooking(req):
    book=bookingdb.objects.all()
    return render(req,'bookingdisplay.html', {'book':book})
def deletebooking(req,dataid):
    data=bookingdb.objects.get(id=dataid)
    data.delete()
    return redirect(displaybooking)


