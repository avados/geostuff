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

"""
Compare 2 objects, recursively sort any lists it finds (and convert dictionaries to lists of (key, value) pairs so that they're orderable):
    """


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def get_default_new_step() -> Step:
    test_step = Step()
    # test_step.id = -1
    test_step.name = 'default step'
    test_step.point = Point(-1, -1)
    test_step.type = StepType.POI
    return test_step


@given("a new step")
def step_impl(context):
    context.test_step = get_default_new_step()


@when("i am saving it")
def step_impl(context):
    # ici il ne faut pas appeler save sur un objet python, il vaut mieux passer par  DRF
    context.test_step.save()


@then("the name must not be empty")
def step_impl(context):
    try:
        assert (Step.objects.get(pk=context.test_step.id) is not None)
    except ValidationError:
        pass


client = APIClient()


@given("i am not an identified user")
def step_impl(context):
    pass


@when("calling the latest version of the api")
def step_impl(context):
    response = client.get('/api/v1/steps/', format='json')
    context.data = response.data

    assert response.status_code == 200


@then("i receive all existing step")
def step_impl(context):
    stepsQuerySet = Step.objects.all()
    stepJsonList = StepSerializer(stepsQuerySet, many=True)
    assert ordered(stepJsonList.data) == ordered(context.data)


@step("i created a new step")
def step_impl(context):
    st = Step.objects.create(point=Point(5, 23), name='new step')
    context.step_id = st.id


@when("calling the latest version of the api with the step id")
def step_impl(context):
    response = client.get('/api/v1/steps/' + str(context.step_id) + '/', format='json')

    assert response.status_code == 200
    context.data = response.data


@then("i receive the specified step")
def step_impl(context):
    stepsQuerySet = Step.objects.get(pk=context.step_id)
    stepJsonList = StepSerializer(stepsQuerySet, many=False)
    assert ordered(stepJsonList.data) == ordered(context.data)


@when("calling the latest version of the api to create a step")
def step_impl(context):
    _step = get_default_new_step()
    # need a fake step id
    _step.id = -1
    serializer = StepSerializer(instance=_step, many=False)
    response = client.post('/api/v1/steps/', data=json.dumps(serializer.data), content_type="application/json")

    assert response.status_code == 201
    context.data = response.data


@then("i receive the newly created step")
def step_impl(context):
    _step = get_default_new_step()
    _step.id = context.data['id']
    step_json_list = StepSerializer(_step, many=False)

    assert ordered(step_json_list.data) == ordered(context.data)


@when("calling the latest version of the api to update a step")
def step_impl(context):
    _step = get_default_new_step()
    _step.save()

    _step.name = 'updated name'
    serializer = StepSerializer(instance=_step, many=False)
    response = client.put('/api/v1/steps/'+str(_step.id)+'/', data=json.dumps(serializer.data), content_type="application/json")

    assert response.status_code == 200
    context.data = response.data


@then("i receive the updated version of the step")
def step_impl(context):
    assert context.data['properties']['name'] == 'updated name'

