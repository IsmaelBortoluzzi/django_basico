from django.urls import path
from core import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact/', views.Contact.as_view(), name='contato'),
    path('produto/<int:pk>', views.ProdutoDetails.as_view(), name='produto'),
]