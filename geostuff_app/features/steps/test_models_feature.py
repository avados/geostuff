from behave import given, when, then, use_step_matcher
from geostuff_app.models import Step
from django.contrib.gis.geos import Point
import logging
from django.core.exceptions import ValidationError

use_step_matcher("re")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@given("a new step")
def step_impl(context):
    test_step = Step()
    test_step.point = Point(5, 23)
    context.test_step = test_step


@when("i am saving it")
def step_impl(context):
    # ici il ne faut pas appeler save sur un objet python, il vaut mieux passer par une form(?) DRF
    context.test_step.save()


@then("the name must not be empty")
def step_impl(context):
    try:
        assert (Step.objects.get(pk=context.test_step.id) is not None)
    except ValidationError:
        pass

