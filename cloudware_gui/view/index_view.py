import logging

import wx

from cloudware_gui.view.base_view import BaseView


class IndexView(BaseView):
    def __init__(self):
        super().__init__()
        wx.Frame.__init__(self, None, -1, '配置中心', size=(160 * 3, 90 * 3))
        panel = wx.Panel(self, -1)

        # 这是一个基本的静态文本  
        wx.StaticText(panel, -1, "This is an example of static text",
                      (100, 10))

        # 指定了前景色和背景色的静态文本  
        rev = wx.StaticText(panel, -1, "Static Text With Reversed Colors",
                            (100, 50))
        rev.SetForegroundColour('white')
        rev.SetBackgroundColour('black')

        # 指定居中对齐的的静态文本  
        center = wx.StaticText(panel, -1, "align center", (100, 50),
                               (160, -1), wx.ALIGN_CENTER)
        center.SetForegroundColour('white')
        center.SetBackgroundColour('black')

        # 指定右对齐的静态文本  
        right = wx.StaticText(panel, -1, "align right", (100, 70),
                              (160, -1), wx.ALIGN_RIGHT)
        right.SetForegroundColour('white')
        right.SetBackgroundColour('black')

        # 指定新字体的静态文本  
        str = "You can also change the font."
        text = wx.StaticText(panel, -1, str, (20, 100))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        # 显示多行文本  
        wx.StaticText(panel, -1, "Your text\ncan be split\n"
                                 "over multiple lines\n\neven blank ones", (20, 150))

        # 显示对齐的多行文本
        wx.StaticText(panel, -1, "Multi-line text\ncan also\n"
                                 "be right aligned\n\neven with a blank", (220, 150),
                      style=wx.ALIGN_RIGHT)
        self.Bind(wx.EVT_CLOSE, self.close)

    def close(self, event):
        logging.info('close')
        self.Show(False)
