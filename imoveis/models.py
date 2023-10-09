from django.db import models

class Imovel(models.Model):
    foto = models.URLField()
    preço = models.CharField(max_length=20)
    endereço = models.CharField(max_length=200)
    metros_quadrados = models.CharField(max_length=10)
    quarto = models.CharField(max_length=2)
    banheiro = models.CharField(max_length=2)
    estacionamento = models.CharField(max_length=2)

    def __str__(self):
        return self.endereço
