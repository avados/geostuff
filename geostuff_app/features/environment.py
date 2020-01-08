import os
import django
from django.test.runner import DiscoverRunner
from django.test.testcases import TestCase

"""
This file setup behave to create a temp database for BDD
"""


os.environ['DJANGO_SETTINGS_MODULE'] = 'geostuff.settings'


def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()

# def before_scenario(context, scenario):
#     context.test = TestCase()
#     context.test.setUpClass()
#
#
# def after_scenario(context, scenario):
#     context.test.tearDownClass()
#     del context.test