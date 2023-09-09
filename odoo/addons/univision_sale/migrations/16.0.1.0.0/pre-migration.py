import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_sale : pre-migration start')

    # # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    # cr.execute("""
    #                DELETE FROM ir_model_data WHERE id=34759
    #        """)
    #
    # cr.execute("""
    #            DELETE FROM ir_model_data WHERE id=34760
    #    """)

    _logger.info('univision_sale : pre-migration end')
