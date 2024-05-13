from django.shortcuts import render,redirect,reverse
from django.views.generic import ListView,DetailView
from .models import Product,Order,Category,TopProduct
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
import decimal

# Create your views here.
def homeview(request):
    topproduct_list = TopProduct.objects.all()
    category_list = Category.objects.all()

    context = {
        'topproducts': topproduct_list,
        'categories': category_list,
    }
    return render(request,'home.html',context)

def productview(request):
    product_list = Product.objects.all()
    search_item = request.GET.get('search_item')

    if search_item != '' and search_item is not None:
        product_list = product_list.filter(Q(name__icontains=search_item) | Q(description__icontains=search_item) | Q(category__name__icontains=search_item))

    paginator = Paginator(product_list,12)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {
        "products": product_list,
    }
    return render(request,'product.html',context)

def filter_products(request, price_range):
    
    if price_range == '0_500':
        product_list = Product.objects.filter(price__range=(0, 500))
    elif price_range == '500_1000':
        product_list = Product.objects.filter(price__range=(500, 1000))
    elif price_range == '1000_10000':
        product_list = Product.objects.filter(price__range=(1000, 10000))
    elif price_range == '10000_up':
        product_list = Product.objects.filter(price__gte=(10000))
    elif price_range == 'all':
        product_list = Product.objects.all()

    if price_range != 'all':
        paginator = Paginator(product_list,6)
        page = request.GET.get('page')
        product_list = paginator.get_page(page)

    context = {
        'products': product_list,
    }
    return render(request, 'product.html', context)

class detailview(DetailView):
    model = Product
    template_name = "detail.html"

def checkoutview(request):
    items = request.POST.get('inputitems')
    name = request.POST.get('Name')
    email = request.POST.get('email')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zipcode = request.POST.get('zipcode')
    total = request.POST.get('total')

    if request.method == "POST":
        order = Order(items=items,name=name,email=email,address=address1,address2=address2,city=city,state=state,zipcode=zipcode,total=total)
        Order.save(order)
        messages.success(request,'Order Successfully Placed.')
        return redirect("/checkout")
    return render(request,"checkout.html")

# ======================= shop =======================

def mobileview(request):
    product_list = Product.objects.filter(category=1)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/mobile.html',context)

def tvview(request):
    product_list = Product.objects.filter(category=2)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/tv.html',context)

def electronicview(request):
    product_list = Product.objects.filter(category=3)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/electronic.html',context)

def fashionview(request):
    product_list = Product.objects.filter(category=4)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/fashion.html',context)

def beautyview(request):
    product_list = Product.objects.filter(category=5)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/beauty.html',context)

def groceryview(request):
    product_list = Product.objects.filter(category=6)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/grocery.html',context)
    
def furnitureview(request):
    product_list = Product.objects.filter(category=7)
    context = {
        "products": product_list,
    }
    return render(request, 'shop/furniture.html',context)