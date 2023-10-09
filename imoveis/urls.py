from django.urls import path
from .views import ImovelList, ImovelDetail, page_list

urlpatterns = [
    path('imoveis/', ImovelList.as_view(), name='imovel-list'),
    path('imoveis/<int:pk>/', ImovelDetail.as_view(), name='imovel-detail'),
    path('imoveis-list/', page_list, name='imoveis-list'),  # Adicione esta linha
]   

