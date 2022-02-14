from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from core.models import Produto


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {'ola': 'ola mundo'}
        return context


class Contact(TemplateView):
    template_name = 'contact.html'


class ProdutoDetails(DetailView):
    model = Produto
    template_name = 'produto_details.html'
    context_object_name = 'produto'


# class Contact(ListView):
#     template_name = 'contact.html'
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs
