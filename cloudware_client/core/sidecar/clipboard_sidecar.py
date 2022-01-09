import io
import logging
import os

from PIL import ImageGrab, Image

from cloudware_client.core.sidecar.base_sidecar import BaseSideCar
from cloudware_client.core.target.clipboard_target import ClipBoardTarget
from cloudware_client.conf.conf import get_base_conf_obj
from cloudware_client.util.clipboard import base_spliter, ClipboardUtil


class ClipBoardSideCar(BaseSideCar):
    """
    PC跨平台的监听剪贴版事件
    """

    def __init__(self, target: ClipBoardTarget):
        self.target = target
        self.last_content = None

    def process(self):
        # 0. sync from remote
        # ClipboardUtil.sync_from_remote()
        content = self.target.fetch_one()
        # 如果为空，可能是图片文件，读出二进制文件
        is_pic = False
        if not content:
            img = ImageGrab.grabclipboard()
            img_bytes = io.BytesIO()
            if isinstance(img, Image.Image):
                img.save(img_bytes, 'png')
                content = img_bytes.getvalue()
                is_pic = True
        # 判断是否可以初始化 self.last_content
        if not self.last_content and ClipboardUtil.get_last_record() != content:
            self.last_content = content
        # 判断是否可以写入 history; 不为空且最后一条和当前不一致
        if content and (self.last_content and content != self.last_content):
            logging.info("latest copy=%s", content)
            # 先替换内存
            self.last_content = content
            # 1. save to localStorage
            n_conf = get_base_conf_obj()
            if not n_conf:
                logging.error("配置不存在")
                exit(0)
            # 不存在历史记录文件，则创建
            if not os.path.exists(n_conf.history_file_path):
                with open(n_conf.history_file_path, 'w') as f:
                    logging.info('init history file')
            if is_pic:
                # TODO 暂时不处理图片
                return
            # TODO 写性能优化
            ClipboardUtil.write_local_history(content, n_conf)
            logging.info('suc sync to history file')
            # 2. sync to remote
            # TODO config switch to control if sync 2 remote
            # ClipboardUtil.sync_to_remote(content, 'text')
        else:
            """
            忽略重复复制
            """
            pass
            # "message from machine 1"