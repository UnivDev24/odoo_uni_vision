import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('UniVision Calendar : pre-migration start')

    # REMOVE ALL VIEWS THAT ARE NOT IN MODULES
    cr.execute("""
               DELETE FROM ir_ui_view WHERE id=1155
       """)

    # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    cr.execute("""
               DELETE FROM ir_model_data WHERE id=69600
       """)

    _logger.info('UniVision Calendar : pre-migration end')