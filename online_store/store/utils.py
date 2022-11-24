from .models import *

class DataMixin:
    def get_context_data(self, **kwargs):
        context = kwargs
        cats = Categories.objects.all()
        cats_types = Cat_types.objects.all()

        context['cats'] = cats
        context['cats_types'] = cats_types
        return context