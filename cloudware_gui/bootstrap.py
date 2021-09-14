import logging
import wx
from manager.gui import GuiManager
from cloudware_gui.conf.conf import check_conf_init
from cloudware_gui.util.log import config_logger

# 初始化日志
config_logger()
# 检查配置文件是否初始化
conf = check_conf_init()
logging.info("conf object is %s", conf.__dict__)

class MainAPP(wx.App):

    def OnInit(self):
        self.manager = GuiManager(self.UpdateUI)
        self.frame = self.manager.get_frame(0)
        self.frame.Show()
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
