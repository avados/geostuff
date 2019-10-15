from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
import geostuff_app.validators.step_validator as step_validator

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Step(models.Model):
    name = models.CharField(max_length=200)
    point = models.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    def clean(self):  # called by django on form saving, not model saving
        step_validator.validate_step(self)