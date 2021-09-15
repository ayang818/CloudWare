from cloudware_gui.view.base_view import BaseView


router = {
    "INDEX": 0,
    "SECOND": 10000
}

frame_mapping = {
    router.get('INDEX'): BaseView,
    router.get('SECOND'): BaseView
}