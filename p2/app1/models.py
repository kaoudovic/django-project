from django.db import models


class staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    age=models.IntegerField()
    birthday=models.DateField()
    department=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
