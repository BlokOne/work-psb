from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required

from shop.models import Product


class Index(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    template_name = 'pages/index.html'


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
