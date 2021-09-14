import wx


class BaseView(wx.Frame):
    """
    任何界面都要支持热键事件
    """
    def __init__(self):
        super().__init__(None, title='', size=(160 * 3, 90 * 3))
        self.hotkey = wx.NewIdRef()  # 创建id
        self.panel = wx.Panel(self)  # 创建面板
        self.RegisterHotKey(self.hotkey, wx.MOD_ALT, wx.WXK_DOWN)  # 注册热键

        self.Bind(wx.EVT_HOTKEY, self.hot_key, id=self.hotkey)  # 绑定热键事件（按alt+down键响应）
        self.panel.Bind(wx.EVT_KEY_DOWN, self.key_event)  # 绑定按键事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)  # 绑定关闭事件

    def key_event(self, event):  # 按键事件 （按shift键响应）
        key = event.GetKeyCode()
        if key == wx.WXK_SHIFT:
            print("按键事件响应")

    def hot_key(self, event):  # 热键事件 （按alt+down键响应）
        print('热键事件响应')

    def OnClose(self, event):  # 关闭事件
        print('注销热键')
        self.UnregisterHotKey(self.hotkey)  # 注销热键
        self.Destroy()  # 销毁窗口

#
# app = wx.App()
# frame = RegistHotKeyWindow()  # 创建窗口
# frame.Center()  # 设置窗口位置
# frame.Show()  # 让窗口显示出来
# app.MainLoop()  # 进入事件循环
