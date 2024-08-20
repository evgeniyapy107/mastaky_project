from django.db import models


class Painting(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    image = models.ImageField(upload_to='paintings/')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class AboutPainting(models.Model):
    painting = models.OneToOneField(Painting, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to='painting_details/')
    image2 = models.ImageField(upload_to='painting_details/')
    image3 = models.ImageField(upload_to='painting_details/')
    image4 = models.ImageField(upload_to='painting_details/')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
