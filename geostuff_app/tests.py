from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.gis import geos

import logging

# Create your tests here.\
from geostuff_app.models import Step

logger = logging.getLogger(__name__)

logger.info('BEGINNING TESTS')


class TestStepValidation(TestCase):
    def setUp(self):
        geom = geos.Point(x=1,y=1)
        self.step = Step.objects.create(name="company1", point= geom)


    def test_validate_step_name_not_empty(self):
        assert self.step.name is not None



