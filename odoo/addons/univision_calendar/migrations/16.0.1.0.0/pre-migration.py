import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('UniVision Calendar : pre-migration start')

    # TO UNINSTALL CUSTOM MODULE
    cr.execute("UPDATE ir_module_module SET state = 'to remove' WHERE name = 'univision_calendar'")

    _logger.info('UniVision Calendar : pre-migration end')