from django.db import models


class Education(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class EducationDetail(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    image_2 = models.FileField(upload_to='images/', default='images/sw_1.jpeg')
    image_3 = models.FileField(upload_to='images/', default='images/sw_1.jpeg')
    description = models.TextField()
    price = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class MK(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class MkDetail(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    image_2 = models.FileField(upload_to='images/', default='images/sw_1.jpeg')
    image_3 = models.FileField(upload_to='images/', default='images/sw_1.jpeg')
    description = models.TextField()
    price = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class StudentWork(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    review_text = models.TextField()

    def __str__(self):
        return self.author

