from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


from . import models
from . import forms

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'userform': forms.userForm(
                data=self.request.POST or None
            ),
            'perfilform': forms.PerfilForm(
                data=self.request.POST or None
            )
            }

        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar
    
class Criar(BasePerfil):
    pass

class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')