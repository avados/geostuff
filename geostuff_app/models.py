from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import geostuff_app.validators.step_validator as step_validator
from enum import IntEnum
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class CustomUser(AbstractUser):
    pass


class StepType(IntEnum):
    ACCOMMODATION = 1
    FOOD = 2
    POI = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Step(models.Model):
    name = models.CharField(max_length=200)
    point = models.PointField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=StepType.choices(), default=StepType.POI)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    def clean(self):  # called by django on form saving, not model saving
        step_validator.validate_step(self)


class Map(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
