import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_sale : pre-migration start')

    _logger.info('univision_sale : pre-migration end')
