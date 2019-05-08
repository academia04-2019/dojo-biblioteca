from django.db import models
from biblioteca.choices import CHOICES_GENERO

class Livro(models.Model):
    titulo = models.CharField()
    lancamento = models.DateField()
    descricao = models.TextField()
    autor = models.Charfield(max_length=256, default='')
    genero = models.charField(max_length=256, choices=CHOICES_GENERO ,default='')

    def __str__(self):
        return self.titulo

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    livro = models.ForeignKey(Livro, on_delete=models.SET_DEFAULT, default='')
