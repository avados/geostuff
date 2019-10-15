import logging

logger = logging.getLogger(__name__)


def validate_step(_step):
    logger.info('POUET')
    if _step.name is None:
        raise BaseException('Name is mandatory')

