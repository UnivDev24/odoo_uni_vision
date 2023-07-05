import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_web : pre-migration start')

    # TO UNINSTALL CUSTOM MODULE
    cr.execute("UPDATE ir_module_module SET state = 'to remove' WHERE name = 'univision_web'")

    _logger.info('univision_web : pre-migration end')

