import logging
_logger = logging.getLogger(__name__)

def migrate(cr, version):

    _logger.info('UniVision Account : pre-migration start')

    # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    cr.execute("""
                       DELETE FROM ir_model_data WHERE id=34756
               """)

    cr.execute("""
                   DELETE FROM ir_model_data WHERE id=34757
           """)

    # REMOVE ALL VIEWS THAT ARE NOT IN MODULES
    cr.execute("""
                       DELETE FROM ir_ui_view WHERE id=1091
               """)

    # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    cr.execute("""
                       DELETE FROM ir_model_data WHERE id=24333
               """)


    _logger.info('UniVision Account : pre-migration end')