from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
# from django.http import HttpResponse
from django.contrib import messages

from produto.models import Variacao
from .models import Pedido, ItemPedido

from utils import utils


class Pagar( DetailView):
    def get(self, *args, **kwargs):
        ...


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        ...
           


class Detalhe(DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'


class Lista(ListView):
    def get(self, *args, **kwargs):
        ...