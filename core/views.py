from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {'ola': 'ola mundo'}
        return context



class Contact(TemplateView):
    template_name = 'contact.html'


# class Contact(ListView):
#     template_name = 'contact.html'
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs
