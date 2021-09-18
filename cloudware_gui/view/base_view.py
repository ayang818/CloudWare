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
        width = 160 * 3
        height = 90 * 3
        # [done] win 被最小化后无法呼出，直接干掉边框
        super().__init__(None, title='CloudWare0.0.1', size=(width, height),
                         style=wx.SIMPLE_BORDER | wx.TRANSPARENT_WINDOW)
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.panel = wx.Panel(self, size=(width, height))

        # 注册快速粘贴快捷键
        self.quickpaste = wx.NewIdRef()
        self.RegisterHotKey(self.quickpaste, wx.MOD_ALT, wx.WXK_DOWN)
        self.Bind(wx.EVT_HOTKEY, self.quick_paste, id=self.quickpaste)

        # 注册关机事件快捷键
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # 关联历史记录
        self.history_record_list = HistoryUtil.batch_get_records(start_pos=0, number=20)

        # 关联ListBox
        self.list_box = wx.ListBox(self.panel, -1, (0, 0), (width, height), self.history_record_list, wx.LB_SINGLE)
        # 绑定键盘按键事件
        self.list_box.Bind(wx.EVT_KEY_DOWN, self.base_keyboard_event)
        # TODO 设置光标
        self.current_idx = 0
        if len(self.history_record_list) > 0:
            self.list_box.SetSelection(self.current_idx)
        self.Center()
        self.Show()

    def base_keyboard_event(self, event):
        key = event.GetKeyCode()
        logging.info("key code=%s", key)
        if key == wx.WXK_ESCAPE:
            logging.info("close frame")
            self.Show(False)
        elif key == wx.WXK_DOWN:
            if self.current_idx <= len(self.history_record_list) - 1:
                self.current_idx += 1
                self.list_box.SetSelection(self.current_idx)
        elif key == wx.WXK_UP:
            if self.current_idx >= 1:
                self.current_idx -= 1
                self.list_box.SetSelection(self.current_idx)
        elif key == 67:
            # 如果是 C，就复制内容到剪贴板里
            pyperclip.copy(self.history_record_list[self.current_idx])


    def quick_paste(self, event):
        """
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
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.SetWindowStyle(wx.SIMPLE_BORDER)
        self.Show(True)

        # self.listBox.SetFocusFromKbd()
        # self.listBox.SetFocus()
        # TODO 写入剪贴板事件
        # pyperclip.copy("some thing")

    # def update_ui(self):
    #     print("update")
    #     ViewUtil.update_view(self, frame_id=INDEX)

    def on_close(self, event):  # 关闭事件
        # print('注销热键')
        # self.UnregisterHotKey(self.quickpaste)  # 注销热键
        # self.Destroy()  # 销毁窗口
        logging.info('close')
        self.Show(False)

