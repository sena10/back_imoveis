from rest_framework import generics
from .models import Imovel
from .serializers import ImovelSerializer
from django.shortcuts import render

class ImovelList(generics.ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer



def page_list(request):
    imoveis = Imovel.objects.all()
    return render(request, 'page.html', {'imoveis': imoveis})