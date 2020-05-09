from django.db import models


class company(models.Model):
    fullname = models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
