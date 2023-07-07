import logging
_logger = logging.getLogger(__name__)

def migrate(cr, version):

    _logger.info('Web favicon : pre-migration start')

    cr.execute("""
               DELETE FROM ir_model_data WHERE id=69260
       """)

    cr.execute("""
                   DELETE FROM ir_model_data WHERE id=69257
           """)

    cr.execute("""
                       DELETE FROM ir_model_data WHERE id=69258
               """)

    cr.execute("""
                           DELETE FROM ir_model_data WHERE id=69259
                   """)

    cr.execute("""
                       DELETE FROM ir_ui_view WHERE id=1149
               """)

    cr.execute("""
                   DELETE FROM ir_ui_view WHERE id=1150
           """)

    cr.execute("""
                      DELETE FROM ir_model_fields WHERE id=9868
              """)

    cr.execute("""
                          DELETE FROM ir_model_fields WHERE id=9869
                  """)


    _logger.info('Web favicon : pre-migration end')