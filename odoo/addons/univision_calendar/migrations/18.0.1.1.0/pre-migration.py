import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('UniVision Calendar : pre-migration start')

    _logger.info('UniVision Calendar : pre-migration end')