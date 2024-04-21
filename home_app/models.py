from django.db import models
from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    TextField,
    BooleanField,
    CASCADE,
    DO_NOTHING
)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)


class Light(models.Model):
    is_on = models.BooleanField(default=False)
    last_activated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Light {'on' if self.is_on else 'off'}"

