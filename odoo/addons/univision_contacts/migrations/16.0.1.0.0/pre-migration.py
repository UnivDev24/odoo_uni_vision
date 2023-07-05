import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('univision_contacts : pre-migration start')

    # inactive old view
    cr.execute("""
            update ir_ui_view v
            set inherit_id = NULL, active = false
            where
            v.id in (1156)
        """)


    _logger.info('univision_contacts : pre-migration end')
