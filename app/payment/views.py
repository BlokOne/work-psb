import requests
from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

from .payment import auth


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            url = auth(float(cart.get_total_price()), str(order.order_id))
            return redirect(url)

    else:
        form = OrderCreateForm
    return render(request, 'pages/orders/created.html',
                  {'cart': cart, 'form': form})
