from djongo import models

class Cards(models.Model):
    titulo = models.CharField(max_length = 200, blank = True)
    codigo = models.CharField(max_length = 30, blank = True)
    data_hora_inserido = models.DateTimeField(auto_now_add = True)
    mais_recente = models.BooleanField(default = True)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    url_imagem_carta = models.TextField()
    url_carta = models.TextField()