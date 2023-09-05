from django.shortcuts import render,redirect
from adminapp.models import categorydb,productdb
from userapp.models import bookingdb,userdb
from django.contrib import messages

# Create your views here.
def homepage(req):
    category = categorydb.objects.all()
    return render(req,'home.html',{'category':category})
def food(req,prod):
    product=productdb.objects.filter(Category_Name=prod)
    return render(req,'foodpage.html',{'product':product})
def singlefoodpage(req,dataid):
    category=categorydb.objects.all()
    product=productdb.objects.filter(id=dataid)
    return render(req,'singlefood.html', {'product':product, 'category':category})
def booking(req):
    return render(req,'Bookingpage.html')
def savebooking(req):
    if req.method=="POST":
        na=req.POST.get('name')
        us=req.POST.get('user')
        em=req.POST.get('email')
        da=req.POST.get('date')
        sp=req.POST.get('special')
        no=req.POST.get('select')
        obj=bookingdb(Name=na,Email=em,Date=da,Chair=no,Request=sp,User=us)
        obj.save()
        messages.success(req,"Congratulations..! Your Booking is Confirmed..!")
        return redirect(booking)
def aboutpage(req):
    return render(req,'about.html')
def userloginpage(req):
    return render(req,'userlogin.html')
def saveuser(req):
    if req.method=="POST":
        na=req.POST.get('fname')
        em=req.POST.get('emails')
        nu=req.POST.get('number')
        ps=req.POST.get('passwords')
        obj=userdb(Name=na,Email=em,Number=nu,Password=ps)
        obj.save()
        messages.success(req, "Congratulations..! User saved")
        return redirect(userloginpage)
def loginuser(req):
    if req.method=="POST":
        usrnme=req.POST.get('email')
        psswrd=req.POST.get('password')
        if userdb.objects.filter(Name=usrnme,Password=psswrd).exists():
            req.session['Username']=usrnme
            req.session['Password']=psswrd
            return redirect(homepage)
        else:
            return redirect(userloginpage)
    else:
        return redirect(userloginpage)
def logout(req):
    del req.session['Username']
    del req.session['Password']
    return redirect(userloginpage)
def cart(req):
    cartt=bookingdb.objects.filter(User=req.session['Username'])
    return render(req,'cartpage.html', {'cartt':cartt})



