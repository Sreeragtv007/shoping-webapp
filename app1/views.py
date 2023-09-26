from django.shortcuts import render
from .models import product,category

# Create your views here.
def index(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    obj=product.objects.filter(categ__name__icontains=q)
    data=category.objects.all()

    

    
    context={'obj':obj,'data':data}
    return render(request,'index.html',context)

def home(request):
    return render(request,'home.html')








