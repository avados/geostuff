from behave import given, when, then, step, use_step_matcher
from geostuff_app.models import Step, StepType, Map
from django.contrib.gis.geos import Point
import logging
from django.core.exceptions import ValidationError
from django.test.utils import get_runner
from rest_framework.test import APIClient
from django.test import Client
from django.urls import reverse
from django.urls import path
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.core import serializers
from geostuff_app.serializers import StepSerializer, MapSerializer
import json
from django.test.runner import DiscoverRunner
import os
import django

use_step_matcher("re")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

client = APIClient()

""" MAP """

def get_default_new_map() -> Map:
    test_map = Map()
    # test_step.id = -1
    test_map.name = 'default step'

    return test_map


@when("calling the latest version of the api to create a map")
def step_impl(context):
    _map = get_default_new_map()

    serializer = MapSerializer(instance=_map, many=False)
    response = client.post('/api/v1/m/', data=json.dumps(serializer.data), content_type="application/json")

    assert response.status_code == 201
    context.data = response.data

@then("i receive the newly created map")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then i receive the newly created map')