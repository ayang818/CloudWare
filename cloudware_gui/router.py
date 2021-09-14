from cloudware_gui.view.base_view import BaseView
from cloudware_gui.view.index_view import IndexView


router = {
    "INDEX": 0,
    "SECOND": 10000
}

frame_mapping = {
    router.get('INDEX'): IndexView,
    router.get('SECOND'): BaseView
}