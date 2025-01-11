import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_contacts : pre-migration start')

    _logger.info('univision_contacts : pre-migration end')
