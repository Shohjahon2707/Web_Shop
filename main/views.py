from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Category, Product
import random
from decimal import Decimal
from .forms import CategoryFilterForm

def home_view(request):
    return render(request, 'main/index.html')


class products_list(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'

class productsdetail_view(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'products'

class productsupdate_view(UpdateView):
    pass





def products_view(request):
    categories = Category.objects.all()
    form = CategoryFilterForm(request.GET or None, categories=categories)
    products = Product.objects.all()

    if form.is_valid():
        category_name = form.cleaned_data.get('category')
        if category_name:
            products = products.filter(category__name=category_name)

    context = {
        'form': form,
        'products': products,
        'categories': categories,
    }
    return render(request, 'main/products.html', context)
    


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    
    if str(pk) in cart:
        cart[str(pk)] += 1
    else:
        cart[str(pk)] = 1

    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = Decimal('0.00')

    for pk, quantity in cart.items():
        product = get_object_or_404(Product, pk=pk)
        product.total_price = product.price * quantity
        product.quantity = quantity
        products.append(product)
        total += product.total_price

    discount_percent = request.session.get('discount_percent', 0)
    discount_amount = total * (Decimal(discount_percent) / Decimal('100'))
    final_total = total - discount_amount

    context = {
        'products': products,
        'total': total,
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'final_total': final_total,
        'you_get_paid': discount_percent > 100,
    }

    return render(request, 'main/cart.html', context)

def apply_discount(request):
    discount = random.randint(0, 101)
    request.session['discount_percent'] = discount
    return redirect('cart')


def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart')
