import requests, uuid, json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


from .models import OrderItem, Order
#from .forms import OrderCreateForm
from cart.cart import Cart
from .payment import auth, check_paid


def order_create(request):
    cart = Cart(request)
    data = auth(float(cart.get_total_price()), str(uuid.uuid4()))
    order = Order(email=request.user.email, invoice_id=data["invoice_id"])
    order.save()
    for item in cart:
        OrderItem.objects.create(order=order,
                                product=item['product'],
                                price=item['price'],
                                quantity=item['quantity'])
    # очистка корзины
    cart.clear()
    return redirect(data["pay_url"])


def order_print(request):
    cart = Cart(request)
    return render(request, 'theme/pages/orders/created.html', {'cart': cart})


@csrf_exempt
def order_success(request):
    if request.method == "GET":
        invoice_id = request.GET.get("invoice_id")[4:]
        if check_paid(invoice_id):
            order = Order.objects.get(invoice_id=invoice_id)
            order.paid = True
            order.save()
            # return JsonResponse({"status": True})
    # return JsonResponse({"status": False})
    return redirect("/")


def order_delete(request):
    invoice_id = request.GET.get("invoice_id")
    if invoice_id:
        Order.objects.filter(invoice_id=invoice_id).delete()
    return redirect("/")