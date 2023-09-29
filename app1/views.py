from django.shortcuts import render,redirect
from .models import product,category
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    obj=product.objects.filter(categ__name__icontains=q)
    data=category.objects.all()


    context={'obj':obj,'data':data}
    return render(request,'index.html',context)

def home(request):
    return render(request,'home.html')

def search_product(request):
    search=request.GET.get('searching')
    
    obj=product.objects.filter(name__icontains=search)
    if obj is not None:
        context={'obj':obj}
        return redirect('index')

    else:

        return render(request,'index.html',context)
    
def register(request):
    if request.POST:
        uname=request.POST.get('username')
        
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username taken")
            return redirect('register')
        elif pass1==pass2:
            user=User.objects.create_user(username=uname,password=pass1)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"password does not match")
            return redirect('register')            
        
            

            
    
    return render(request,'register.html')

def login(request):
     
    return render(request,'login.html')








