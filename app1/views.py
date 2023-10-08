from django.shortcuts import redirect, render
from .models import Product, category, Review, Cart
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# category list


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    o = Product.objects.filter(categ__name__icontains=q)
    d = category.objects.all()
    #count = Cart.objects.filter(user=request.user)

    context = {'o': o, 'd': d, 'cart': cart}
    return render(request, 'index.html', context)


# searching by product name
def search_product(request):
    qu = None
    pr = None
    if 'qu' in request.GET:
        qu = request.GET.get('qu')
        print(qu)
        pr = Product.objects.filter(name__icontains=qu)
        print(pr)
        context = {'pr': pr}
        return render(request, 'product.html', context)
    else:

        return render(request, 'index.html')


def register(request):
    if request.POST:
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username=uname).exists():
            messages.info(request, "user name taken")
            return redirect('register')

        elif pass1 == pass2:
            user = User.objects.create_user(username=uname, password=pass1)
            return redirect('login')
        else:
            messages.info(request, "password does not match")
            return redirect('register')

    return render(request, 'register.html')


def login_user(request):
    if request.POST:
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "user name or password is incorrect")
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request,'login.html')


def productDetails(request, pk):
    data = Product.objects.get(id=pk)
    obj = data.review_set.all()
    if request.POST:
        result = request.POST.get("review")
        print(result)

        review = Review.objects.create(
            review_body=result, user=request.user, product=data)
        return redirect('productdetails', pk=data.id)

    context = {'data': data, 'obj': obj}

    return render(request, 'productdetails.html', context)


def cart(request, pk):
    try:
    
        obj=Product.objects.get(id=pk)
        cart=Cart.objects.create(user=request.user,product=obj)
        messages.info(request,"product added to cart")
        return redirect('productdetails',pk=obj.id)
    except:
        messages.info(request,"product alredy added")
        return redirect('productdetails',pk=obj.id)
    


def cartdeatil(request):

    cart = Cart.objects.filter(user=request.user)
    print(cart)
    
    if len(cart)==0:
        return redirect('index')
    else:
        context={'cart':cart}
   
    return render(request, 'cart.html',context)


def removeCart(request, pk):

    cart = Cart.objects.get(id=pk)
    cart.delete()

    return redirect('cartdetail')


def reviewDelet(request, pk):
    
    review=Review.objects.get(id=pk)
    if review.user.id==request.user.id:
        review.delete()
        return redirect('productdetails', pk=review.product.id)
    else:
        return redirect('productdetails',pk=review.product.id)


    
    