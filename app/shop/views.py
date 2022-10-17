from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required

from shop.models import Product


class Index(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    template_name = 'index.html'
    model = Product


class Shops(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'shop.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 8


class Support(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'support.html'
