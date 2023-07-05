import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_web : pre-migration start')

    # REMOVE ALL VIEWS THAT ARE NOT IN MODULES
    cr.execute("""
                   DELETE FROM ir_ui_view WHERE id=1094
           """)

    # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    cr.execute("""
                   DELETE FROM ir_model_data WHERE id=24336
           """)


    _logger.info('univision_web : pre-migration end')

