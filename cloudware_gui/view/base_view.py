import logging
import sys

import wx
from cloudware_client.core.sidecar.clipboard_sidecar import HistoryUtil
from cloudware_gui.util.view import ViewUtil
from cloudware_gui.const.router_const import INDEX, EMPTY
import pyperclip


class BaseView(wx.Frame):
    """
    任何界面都要支持热键事件
    """

    def __init__(self):
        # 初始化大小
        self.width = 200 * 3
        self.height = 150 * 3
        super().__init__(None, title='CloudWare0.0.1', size=(self.width, self.height),
                         style=wx.SIMPLE_BORDER | wx.TRANSPARENT_WINDOW)
        self.SetMaxSize((self.width, self.height))
        self.SetMinSize((self.width, self.height))
        self.panel = wx.Panel(self, size=(self.width, self.height))

        # 注册快速粘贴快捷键
        self.quickpaste = wx.NewIdRef()
        self.RegisterHotKey(self.quickpaste, wx.MOD_ALT, wx.WXK_DOWN)
        self.Bind(wx.EVT_HOTKEY, self.quick_paste, id=self.quickpaste)

        # 注册关闭事件：关闭事件不关闭进程
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # 初始化列表框
        self.history_record_list = []
        self.current_idx = 0
        self.list_box = wx.ListBox(self.panel, -1, (0, 0), (self.width, self.height),
                                   self.history_record_list,
                                   wx.LB_SINGLE)
        self.update_history_list_box(start_pos=0, number=20)

        # 绑定键盘按键事件
        self.list_box.Bind(wx.EVT_KEY_DOWN, self.base_keyboard_event)

        self.Center()
        self.Show()

    def base_keyboard_event(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            logging.info("close frame")
            self.Show(False)
        elif key == wx.WXK_DOWN:
            if self.current_idx < len(self.history_record_list) - 1:
                self.current_idx += 1
                self.list_box.SetSelection(self.current_idx)
        elif key == wx.WXK_UP:
            if self.current_idx >= 1:
                self.current_idx -= 1
                self.list_box.SetSelection(self.current_idx)
        elif key == 67:
            # 如果是 C，就复制内容到剪贴板里，然后关闭
            pyperclip.copy(self.history_record_list[self.current_idx])
            self.Show(False)

    def quick_paste(self, event):
        """
        :param event:
        :return:
        """
        logging.info('呼出快速粘贴')
        self.update_history_list_box(start_pos=0, number=20)

        # 响应热键事件
        if sys.platform == 'win32':
            self.SetWindowStyle(wx.STAY_ON_TOP | wx.SIMPLE_BORDER)
        elif sys.platform == 'darwin':
            self.SetWindowStyle(wx.STAY_ON_TOP)
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.SetWindowStyle(wx.SIMPLE_BORDER)
        self.Show(True)

        # self.listBox.SetFocusFromKbd()
        self.list_box.SetFocus()

    def update_history_list_box(self, start_pos, number):
        # init or reInit
        self.history_record_list = HistoryUtil.batch_get_records(start_pos, number)
        self.current_idx = 0
        if not self.list_box:
            self.list_box = wx.ListBox(self.panel, -1, (0, 0), (self.width, self.height), self.history_record_list,
                                       wx.LB_SINGLE)
        self.list_box.Clear()
        # update into view
        for item in self.history_record_list:
            self.list_box.Append(item)
        if len(self.history_record_list) > 0:
            self.list_box.SetSelection(self.current_idx)

    def on_close(self, event):  # 关闭事件
        # print('注销热键')
        # self.UnregisterHotKey(self.quickpaste)  # 注销热键
        # self.Destroy()  # 销毁窗口
        logging.info('close')
        self.Show(False)
