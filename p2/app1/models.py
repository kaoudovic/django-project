from django.db import models
from django.contrib.auth.models import User


class staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    age=models.IntegerField()
    birthday=models.DateField()
    department=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name


#link between two table info and User
class info(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)     #username is object from user
    jobs=models.CharField(max_length=50)
    lang=models.CharField(max_length=50)
    num=models.IntegerField()

