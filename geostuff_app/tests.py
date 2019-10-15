from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

import logging

# Create your tests here.\
from geostuff_app.models import Step

logger = logging.getLogger(__name__)

logger.info('BEGINNING TESTS')


class TestStepValidation(TestCase):
    def setUp(self):
        Step.objects.create(name="company1")


    def test_validate_step_name_not_empty(self):
        logger.info('POUET')
        if _step.name is None:
            raise BaseException('Name is mandatory')


