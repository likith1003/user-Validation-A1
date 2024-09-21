from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    add = models.CharField(max_length=50)
    un = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def __str__(self):
        return self.name