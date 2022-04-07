from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    score = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'.title()


class Currency(models.Model):
    code = models.CharField(max_length=200)
    value = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code}: {self.value}'
