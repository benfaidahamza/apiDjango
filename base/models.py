from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
