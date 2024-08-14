from django.db import models

# Create your models here.

class contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + self.last_name