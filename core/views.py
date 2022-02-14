from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from core.models import Produto, Contact


class Index(TemplateView):
    template_name = 'index.html'
    produtos = Produto.objects.all()

    def get_context_data(self, **kwargs):
        context = {'produtos': self.produtos}
        return context


class Contact(ListView):
    model = Contact
    template_name = 'contact.html'

    def get_queryset(self):
        super().get_queryset()


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
