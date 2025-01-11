import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('website_univision : pre-migration start')

    _logger.info('website_univision : pre-migration end')