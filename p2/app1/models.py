from django.db import models


class staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    age=models.IntegerField()
    birthday=models.DateField()

    def __str__(self):
        return self.name
