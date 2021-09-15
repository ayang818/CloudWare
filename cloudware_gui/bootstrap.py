from cloudware_client.core import target
import logging
import wx
from wx.core import App
from manager.view_manager import ViewManager
from cloudware_gui.conf.conf import check_conf_init
from cloudware_gui.util.log import config_logger
from cloudware_client.bootstrap import start
import threading
from cloudware_gui.conf.conf import get_base_conf_obj

# 初始化日志
config_logger()
# 检查配置文件是否初始化
check_conf_init()
conf = get_base_conf_obj()
# import 这个 app 做操作
app = None
logging.info("conf object is %s", conf.__dict__)


class MainAPP(wx.App):

    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_CHINESE)
        self.manager = ViewManager()
        self.frame = self.manager.get_frame(0)
        self.frame.Show()
        # 启动后台监听剪贴板进程
        thread_listener = threading.Thread(target=start)
        thread_listener.setDaemon(True)
        thread_listener.start()
        return True

    def UpdateUI(self, frame_id):
        self.frame.Show(False)
        self.frame = self.manager.get_frame(frame_id)
        self.frame.Show(True)


def main():
    app = MainAPP()
    app.MainLoop()


if __name__ == '__main__':
    main()
