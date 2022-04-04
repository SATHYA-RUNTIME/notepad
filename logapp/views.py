from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from logapp import models
from logapp.models import register,data
from django.contrib import messages
import datetime



# Create your views here.
def login(request):
    
    red="INVALID ENTRY"
    if request.method=="POST":
        global usnamegal
        global felt
        usnamegal=request.POST['uns']
        felt=usnamegal[0]
        
        passwd=request.POST['password']
        if register.objects.filter(username=usnamegal) and register.objects.filter(pwd=passwd):
            return redirect('npda')
        else:
            return render(request,"tmp1/login.html",{"col":red})

    return render(request,"tmp1/login.html")
        

def np(req):
    if req.method=="POST":
        dta=req.POST['datas']
        dt=datetime.datetime.now()
        dd=dt.strftime("%d-%m-%y")
        t=dt.strftime("%H-%M-%S")
        data(npuname=usnamegal,npnots=dta,date=dd,time=t).save()
    olddata=data.objects.filter(npuname=usnamegal)
    return render(req,"tmp1/notepad.html",{"fl":felt,"un":usnamegal,"old":olddata})


def reg(req):
    msg="username already taken"
    
   
    if req.method=="POST":
        un=req.POST['uname']
        mno=req.POST['mno']
        age=req.POST['age']
        gen=req.POST['gender']
        mail=req.POST['mail']
        nk=req.POST['nname']
        pw=req.POST['pwd']
        if register.objects.filter(username=un):
            return render(req,"tmp1/register.html",{"ivalid":msg})       
        else:     
            register(username=un,mobileno=mno,age=age,gender=gen,mail=mail,nikename=nk,pwd=pw).save()
            return redirect('login')
    return render(req,"tmp1/register.html")

def pop(req):
    dttime=data.objects.filter(npuname=usnamegal)
    return render(req,"tmp1/popup.html",{"dtime":dttime})
def detail(request):
    return(request,"tmp1/detail.html")

def delete(request,id):
    deldta=data.objects.get(id=id)
    deldta.delete()
    return redirect('/popup')

def update(request,id):
    deldta=data.objects.get(id=id)
    if request.method=="POST":
        dt=datetime.datetime.now()
        dd=dt.strftime("%d-%m-%y")
        t=dt.strftime("%H-%M-%S")
        updata=request.POST['datas2']
        data(npuname=usnamegal,npnots=updata,date=dd,time=t).save()
        deldta.delete()
        return redirect('/popup')
    return render(request,"tmp1/update.html",{"dts":deldta})
