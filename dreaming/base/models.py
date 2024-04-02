"""
Este módulo contém os modelos das entidades do sistema.
"""
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Work(models.Model):
    """Esse modelo representa as obras literarias."""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    kind = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        """ordena apartir do tipo da obra literaria."""
        ordering = ['kind']

        @staticmethod
        def change_image(new_image):
            """função de modificar o imagem da obra."""
            print(f'teste: {new_image}')

        @staticmethod
        def rename(new_name):
            """função de renomear o tipo da obra."""
            print(f'teste: {new_name}')


class Challenge(models.Model):
    """Esse modelo representa os desafios de leitura."""
    book = models.ForeignKey(Work, related_name='challenges', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        """ordena apartir do valor do campo completed."""
        ordering = ['completed']

        @staticmethod
        def change_book(new_book):
            """função de modificar a obra do desafio de leitura."""
            print(f'teste: {new_book}')

        @staticmethod
        def rename(new_name):
            """função de renomear o titulo do desafio de leitura."""
            print(f'teste: {new_name}')


class Review(models.Model):
    """Esse modelo representa as resenhas dos usuarios a uma obra."""
    work = models.ForeignKey(Work, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True,
                              validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return str(self.title)

    class Meta:
        """ordena apartir da nota das resenhas dos usuarios a obra."""
        ordering = ['score']

        @staticmethod
        def change_book(new_score):
            """função de modificar a nota da resenha do usuario."""
            print(f'teste: {new_score}')

        @staticmethod
        def rename(new_name):
            """função de renomear o titulo da resenha."""
            print(f'teste: {new_name}')


class Journal(models.Model):
    """Esse modelo representa as entradas do diario de progresso de um desafio literario."""
    challenge = models.ForeignKey(Challenge, related_name='journals', on_delete=models.CASCADE)
    entry_name = models.CharField(max_length=200, null=True)
    entry = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.entry)
