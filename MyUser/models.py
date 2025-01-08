from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    entries = models.IntegerField(default=0, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

