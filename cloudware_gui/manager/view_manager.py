# coding=utf-8
import importlib
import os

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
        """
        懒加载 frame
        :param frame_id:
        :return:
        """
        klass_name = self.frame_mapping.get(frame_id, None)
        view_instance = None
        routedir_path = os.path.join(os.path.dirname(__file__), '../view')
        for file in os.listdir(routedir_path):
            # 如果是个python文件，就import成一个module
            if '.py' not in str(file):
                continue
            # 干掉 python 后缀，file名为 xxx.py
            module = importlib.import_module('view.%s' % (file[:-3]))
            for klass, value in module.__dict__.items():
                if str(klass) == klass_name:
                    view_instance = value()
        return view_instance
