import wx


class EmptyView(wx.Frame):

    def __init__(self):
        super().__init__()
        wx.Frame.__init__(self, None, -1, '配置中心', size=(160 * 3, 90 * 3))