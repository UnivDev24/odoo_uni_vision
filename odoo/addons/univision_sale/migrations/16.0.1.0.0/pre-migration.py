import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_sale : pre-migration start')

    # REMOVE ALL VIEWS THAT ARE NOT IN MODULES
    # cr.execute("""
    #            DELETE FROM ir_actions_report WHERE id=421
    #    """)
    #
    # cr.execute("""
    #                DELETE FROM ir_actions_report WHERE id=422
    #        """)

    # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    cr.execute("""
                   DELETE FROM ir_model_data WHERE id=34759
           """)

    cr.execute("""
               DELETE FROM ir_model_data WHERE id=34760
       """)

    _logger.info('univision_sale : pre-migration end')
