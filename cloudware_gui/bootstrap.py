import wx
from manager.gui import GuiManager


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
