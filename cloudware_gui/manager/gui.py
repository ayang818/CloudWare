# coding=utf-8
from cloudware_gui.view import hot_key, setting


class GuiManager(object):
    def __init__(self, update_ui):
        self.update_ui = update_ui
        # 用来装载已经创建的Frame对象
        self.frame_holder = {}

    def get_frame(self, frame_id):
        frame = self.frame_holder.get(frame_id)

        if frame is None:
            frame = self.create_frame(frame_id)
            self.frame_holder[frame_id] = frame

        return frame

    def create_frame(self, frame_id):
        if frame_id == 0:
            # return setting.(parent=None, id=frame_id, UpdateUI=self.update_ui)
            pass
        elif frame_id == 1:
            return contentFrame.ContentFrame(parent=None, id=frame_id, UpdateUI=self.update_ui)
