# coding=utf-8
from cloudware_gui.router import frame_mapping

class ViewManager(object):
    def __init__(self):
        # 用来装载已经创建的Frame对象
        self.frame_holder = {}
        self.frame_mapping = frame_mapping

    def get_frame(self, frame_id):
        frame = self.frame_holder.get(frame_id)
        # 懒加载 frame
        if frame is None:
            frame = self.create_frame(frame_id)
            self.frame_holder[frame_id] = frame
        return frame

    def create_frame(self, frame_id):
        return self.frame_mapping.get(frame_id, None)()
