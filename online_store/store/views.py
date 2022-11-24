from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from .utils import *


def home(request, url):
    return HttpResponse(str(url))


class ProductsList(DataMixin, ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title='Хрустик топ')
        context.update(c_def)
        return context
