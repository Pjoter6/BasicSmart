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


class Category(models.Model):
    name = models.CharField(max_length=100)


class Movie(Model):
    title = CharField(max_length=128)
    rating = IntegerField()
    release_date = DateField()
    description = TextField(null=True)
    created_entry = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title