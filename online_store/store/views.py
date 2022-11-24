from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from .utils import *


# def home(request):
#     return render(request, 'store/base.html')

class ProductsList(DataMixin, ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Хрустик Стор'
        return context
