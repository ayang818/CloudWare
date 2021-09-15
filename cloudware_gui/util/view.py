import wx
from cloudware_gui.manager.view_manager import ViewManager

view_manager = ViewManager()


class ViewUtil(object):
    @classmethod
    def update_view(cls, view: wx.Frame = None, frame_id=0) -> wx.Frame:
        if view:
            view.Show(False)
        view = view_manager.get_frame(frame_id)
        return view
