import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('website_univision : pre-migration start')

    # # REMOVE ALL VIEWS THAT ARE NOT IN MODULES
    # cr.execute("""
    #                      DELETE FROM ir_ui_view WHERE id NOT IN(SELECT res_id FROM ir_model_data WHERE model='ir.ui.view' ORDER BY module)
    #              """)
    #
    # # REMOVE VIEWS THAT ARE NOT USED ANYMORE
    # cr.execute("""
    #                      UPDATE ir_ui_view SET active = True WHERE id IN
    #                      (SELECT res_id FROM ir_model_data WHERE model = 'ir.ui.view' AND module in ('website_univision'))
    #              """)
    #
    # # REMOVE ALL ACT WINDOWS THAT ARE NOT IN MODULES
    # cr.execute("""
    #                      DELETE FROM ir_act_window WHERE id NOT IN (SELECT res_id FROM ir_model_data WHERE model = 'ir.actions.act_window')
    #              """)
    #
    # # REMOVE ACT WINDOWS THAT ARE NOT USED ANYMORE
    # cr.execute("""
    #                      DELETE FROM ir_model_data WHERE model = 'ir.actions.act_window' AND module IN ('website_univision')
    #              """)
    #
    # # TO UNINSTALL CUSTOM MODULE
    # cr.execute("""
    #                      UPDATE ir_module_module SET state = 'to remove' WHERE name = 'website_univision'
    #              """)

    _logger.info('website_univision : pre-migration end')