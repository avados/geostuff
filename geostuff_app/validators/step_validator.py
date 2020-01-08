import logging

logger = logging.getLogger(__name__)


def validate_step(_step):
    if (_step['name'] is None) or (len(_step['name']) == 0):
        raise BaseException('Name is mandatory')

