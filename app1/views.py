from django.shortcuts import redirect, render
from .models import product,category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    obj=product.objects.filter(categ__name__icontains=q)
    data=category.objects.all()


    context={'obj':obj,'data':data}
    return render(request,'index.html',context)



def search_product(request):
    search=request.GET.get('searching')
    obj=product.objects.filter(name__icontains=search )
    
    context={'obj':obj}
    return render (request,'index.html',context)
    

def register(request):
    if request.POST:
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if User.objects.filter(username=uname).exists():
            messages.info(request,"user name taken")
            return redirect('register')

        elif pass1==pass2:
            user=User.objects.create_user(username=uname,password=pass1)
            return redirect('login') 
        else:
            messages.info(request,"password does not match")
            return redirect('register')
        
    return render(request,'register.html')

def login_user(request):
    if request.POST:
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"user name or password is incorrect")
            return redirect('login')
            
        
    
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return render(request,'login.html')










