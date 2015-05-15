from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, RequestProduct


# @login_required()
def home(request):
    if request.user.is_authenticated():
        products = Product.objects.filter(is_active=True)
        data = {'products': products}
        return render(request, 'products_list.html', data)
    else:
        return render(request, 'index.html')

@login_required()
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        requested = RequestProduct.objects.get(product_id=product_id, user=request.user.id)
    except RequestProduct.DoesNotExist:
        requested = None
    data = {'product': product, 'requested': requested}
    return render(request, 'product.html', data)


def add_request(request, product_id):
    if request.POST:
        p = Product.objects.get(id=product_id)
        RequestProduct.objects.create(user=request.user, product=p)
        return redirect('home')
    else:
        return redirect('home')


def requested(request):
    requested = RequestProduct.objects.filter(user=request.user)
    last_requested = RequestProduct.objects.filter(user=request.user)
    latest = last_requested.latest('id')
    data = {'requested': requested, 'latest': latest}
    return render(request, 'requested.html', data)