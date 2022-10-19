import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        print(cd)
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


class Cart_Detail(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'pages/cart/cart.html'

    def get(self, request):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})


class Checkout(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'pages/cart/checkout.html'

    def get_context_data(self, **kwargs):
        api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjY4NCwiZXhwIjo4ODA2NTkxOTU4NX0.fTA4NbQnl_-MD7W1Os2mAYqFow_5n1hiXUUAtbifHno'
        shop_id = 'Hz7LH3DF6ddE1WuU'
        order_id = uuid.uuid4()
        currency = "USD"
        context = {
            "api_key": api_key,
            "shop_id": shop_id,
            "order_id": order_id,
            "currency": currency,
        }
        return context

