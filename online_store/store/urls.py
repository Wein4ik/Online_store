from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductsList.as_view(), name='home'),
    path('type/<slug:url>', home, name='type'),
]
