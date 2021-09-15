import logging
import wx
from cloudware_client.core.sidecar.clipboard_sidecar import 

class BaseView(wx.Frame):
    """
    任何界面都要支持热键事件
    """
    def __init__(self):
        super().__init__(None, title='配置中心', size=(160 * 3, 90 * 3))
        self.panel = wx.Panel(self)
        self.quickpaste = wx.NewIdRef()
        # 注册快速粘贴快捷键
        self.RegisterHotKey(self.quickpaste, wx.MOD_ALT, wx.WXK_DOWN)
        self.Bind(wx.EVT_HOTKEY, self.quick_paste, id=self.quickpaste)
        # 注册关机事件快捷键
        self.Bind(wx.EVT_CLOSE, self.on_close)
        # 关联上历史记录
        colorList = ["红", "绿", "蓝", "白", "紫"]
        # 关联ListBox
        self.listBox = wx.ListBox(self.panel,-1,(10,10),(80,110),colorList,wx.LB_SINGLE)
        self.listBox.SetSelection(2)

        

    def quick_paste(self, event):
        logging.info('呼出快速粘贴')
        self.update_ui()
        self.Show(True)
        # 响应热键事件
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
    
    def update_ui(self):
        pass

    def on_close(self,event):  # 关闭事件
        # print('注销热键')
        # self.UnregisterHotKey(self.quickpaste)  # 注销热键
        # self.Destroy()  # 销毁窗口
        logging.info('close')
        self.Show(False)      

#
# app = wx.App()
# frame = BaseView()  # 创建窗口
# frame.Center()  # 设置窗口位置
# frame.Show()  # 让窗口显示出来

# app.MainLoop()  # 进入事件循环