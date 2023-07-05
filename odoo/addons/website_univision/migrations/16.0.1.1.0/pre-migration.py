import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('website_univision : pre-migration start')

    # TO UNINSTALL CUSTOM MODULE
    cr.execute("UPDATE ir_module_module SET state = 'to remove' WHERE name = 'website_univision'")

    _logger.info('website_univision : pre-migration end')