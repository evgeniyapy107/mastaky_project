from django.db import models


class Painting(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    image = models.ImageField(upload_to='paintings/')  # Поле для изображения картины
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class AboutPainting(models.Model):
    painting = models.OneToOneField(Painting, on_delete=models.CASCADE)
    description = models.TextField()
    image1 = models.ImageField(upload_to='painting_details/')  # Поле для первого изображения
    image2 = models.ImageField(upload_to='painting_details/')  # Поле для второго изображения
    image3 = models.ImageField(upload_to='painting_details/')  # Поле для третьего изображения
    image4 = models.ImageField(upload_to='painting_details/')  # Поле для четвертого изображения

    def __str__(self):
        return self.painting
