from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

from shop.forms import *
from shop.models import Product, Country
from payment.models import Order


class Index(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Order
    context_object_name = 'orders'
    template_name = 'theme/pages/index.html'


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
    template_name = 'theme/pages/shop.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        country = Country.objects.all()
        product = Product.objects.all().order_by('?')[0:4]
        context = super().get_context_data(**kwargs)
        context["country"] = country
        context["product"] = product
        return context


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
    template_name = 'theme/pages/orders/detail.html'


class Settings(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'theme/pages/editprofile.html'

    def get(self, request):
        npd = NewPersonalData(instance=request.user)
        du = DeleteUser()
        context = {"npd": npd, 'du': du}
        return render(request, self.template_name, context)

    def post(self, request):
        p = request.POST
        npd_post = {'csrfmiddlewaretoken': p.get('csrfmiddlewaretoken'), 'username': p.get('username'), 'email': p.get('email')}
        old_npd = NewPersonalData(npd_post, instance=request.user)
        du_post = {'csrfmiddlewaretoken': p.get('csrfmiddlewaretoken'), 'check': p.get('check')}
        old_du =  DeleteUser(du_post)
        if old_npd.is_valid():
            old_npd.save()
        if du_post['check'] and old_du.is_valid():
            User.objects.filter(username=request.user.username).delete()
            return redirect("/")
        npd = NewPersonalData(instance=request.user)
        du = DeleteUser()
        context = {"npd": npd, 'du': du, "old_npd": old_npd}
        return render(request, self.template_name, context)