import logging
import sys

import wx
from cloudware_client.core.sidecar.clipboard_sidecar import HistoryUtil
from cloudware_gui.util.view import ViewUtil
from cloudware_gui.const.router_const import INDEX, EMPTY


class BaseView(wx.Frame):
    """
    任何界面都要支持热键事件
    """

    def __init__(self):
        width = 160 * 3
        height = 90 * 3
        super().__init__(None, title='CloudWare0.0.1', size=(width, height), style=wx.SIMPLE_BORDER|wx.TRANSPARENT_WINDOW)
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.panel = wx.Panel(self, size=(width, height))
        self.quickpaste = wx.NewIdRef()
        # 注册快速粘贴快捷键
        self.RegisterHotKey(self.quickpaste, wx.MOD_ALT, wx.WXK_DOWN)
        self.Bind(wx.EVT_HOTKEY, self.quick_paste, id=self.quickpaste)
        # 注册关机事件快捷键
        self.Bind(wx.EVT_CLOSE, self.on_close)
        # 关联历史记录
        self.history_record_list = HistoryUtil.batch_get_records(start_pos=0, number=10)
        # 关联ListBox
        self.listBox = wx.ListBox(self.panel, -1, (0, 0), (160 * 3, 90 * 3), self.history_record_list, wx.LB_SINGLE)
        self.Bind(wx.EVT_ICONIZE, self.iconize)
        # TODO 设置光标
        if len(self.history_record_list) > 0:
            self.listBox.SetSelection(0)
        self.Center()

    def quick_paste(self, event):
        """
        TODO win 被最小化后无法呼出
        :param event:
        :return:
        """
        logging.info('呼出快速粘贴')
        # self.Close()
        # self.update_ui()
        # 响应热键事件
        if sys.platform == 'win32':
            self.SetWindowStyle(wx.STAY_ON_TOP | wx.SIMPLE_BORDER)
        elif sys.platform == 'darwin':
            self.SetWindowStyle(wx.STAY_ON_TOP)
        self.SetWindowStyle(wx.SIMPLE_BORDER)
        self.Show(True)

    # def update_ui(self):
    #     print("update")
    #     ViewUtil.update_view(self, frame_id=INDEX)

    def on_close(self, event):  # 关闭事件
        # print('注销热键')
        # self.UnregisterHotKey(self.quickpaste)  # 注销热键
        # self.Destroy()  # 销毁窗口
        logging.info('close')
        self.Show(False)

    def iconize(self, event):
        logging.info('iconize')


#
# app = wx.App()
# frame = BaseView()  # 创建窗口
# frame.Center()  # 设置窗口位置
# frame.Show()  # 让窗口显示出来

# app.MainLoop()  # 进入事件循环
