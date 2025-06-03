from django.db import models


class Client(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    nascimento = models.DateField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

