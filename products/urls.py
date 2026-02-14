from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products'),
    path('show', views.show, name='product'),
]
