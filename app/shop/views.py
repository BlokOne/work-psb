from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


from shop.forms import CustomUserCreationForm
from shop.models import Product
from payment.models import Order


class Index(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Order
    context_object_name = 'orders'
    template_name = 'pages/index.html'


def Register(request):
    if request.method == "GET":
        return render(request, "registration/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "registration/register.html",
                {"form": CustomUserCreationForm, "info_errors": list(form.errors.values())},
            )


class Shops(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'pages/shop.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 8


class ShopDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Product
    context_object_name = 'product'
    template_name = 'pages/shop-description.html'


class Support(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'pages/support.html'


class DetailOrder(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Order
    context_object_name = 'order'
    template_name = 'pages/orders/detail.html'

"""
def DetailOrder(request, invoice_id):
    return render(request, "pages/orders/detail.html")
"""