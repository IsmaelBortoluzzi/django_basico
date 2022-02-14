from django.contrib import admin
from core.models import Produto, Contact


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contact)
