import requests, uuid, json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

from .payment import auth, check_paid


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            data = auth(float(cart.get_total_price()), str(uuid.uuid4()))
            order = Order(email=form.cleaned_data.get("email"), invoice_id=data["invoice_id"])
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return redirect(data["pay_url"])

    else:
        form = OrderCreateForm
    return render(request, 'pages/orders/created.html',
                  {'cart': cart, 'form': form})


@csrf_exempt
def order_success(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data = json.loads(data)
        invoice_id = data.get("invoice_id")
        if check_paid(invoice_id):
            order = Order.objects.get(invoice_id=invoice_id)
            order.paid = True
            order.save()
            return JsonResponse({"status": True})
    return JsonResponse({"status": False})
