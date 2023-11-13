from django.urls import path
from .views import ImovelList, ImovelDetail, page_list, detalhe_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('imoveis/', ImovelList.as_view(), name='imovel-list'),
    path('imoveis/<int:pk>/', ImovelDetail.as_view(), name='imovel-detail'),
    path('', page_list, name='imoveis-list'),  
    path('detalhe-list', detalhe_list, name='detalhe-list'),
]


