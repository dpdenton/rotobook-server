from django.db import models

class Employee(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

