import logging
import threading

import wx
import sys, os
os.path.abspath(os.path.dirname(__file__))
print()
sys.path.insert(0, os.path.dirname(__file__) + '/../')

from cloudware_client.bootstrap import start
from cloudware_client.conf.conf import check_conf_init
from cloudware_client.conf.conf import get_base_conf_obj
from cloudware_gui.const.router_const import INDEX
from cloudware_gui.util.log import config_logger
from cloudware_gui.util.view import ViewUtil

# 初始化日志
config_logger()
# 检查配置文件是否初始化
check_conf_init()
conf = get_base_conf_obj()
# import 这个 app 做操作
logging.info("conf object is %s", conf.__dict__)


class MainAPP(wx.App):

    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_CHINESE)
        view = ViewUtil.update_view(frame_id=INDEX)
        # view.Show(False)
        # 启动后台监听剪贴板进程
        thread_listener = threading.Thread(target=start)
        thread_listener.setDaemon(True)
        thread_listener.start()
        return True


app: MainAPP = None


def main():
    global app
    app = MainAPP()
    app.MainLoop()


if __name__ == '__main__':
    from cloudware_client.util.account import AccountUtil

    logging.info("USER_ID=%s; DEVICE_ID=%s; SECRET_KEY=%s", AccountUtil.get_user_id(), AccountUtil.get_device_id(),
                 AccountUtil.get_secret_key())
    main()
