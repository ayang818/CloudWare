import io
import logging
import os

from PIL import ImageGrab, Image
from file_read_backwards import FileReadBackwards

from cloudware_client.core.sidecar.base_sidecar import BaseSideCar
from cloudware_client.core.target.clipboard_target import ClipBoardTarget
from cloudware_gui.conf.conf import get_base_conf_obj

base_spilter = "|.#.#.#.#.|\n"


class ClipBoardSideCar(BaseSideCar):
    """
    PC跨平台的监听剪贴版事件
    """

    def __init__(self, target: ClipBoardTarget):
        self.target = target
        self.last_content = None

    def process(self):
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
        # 判断是否可以写入 history
        if content and (not self.last_content or content != self.last_content):
            logging.info("lastest copy=%s", content)
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
            with open(n_conf.history_file_path, 'a') as f:
                f.write(content + '\n' + base_spilter)
            logging.info('suc sync to history file')
            # 2. send to remote
        else:
            """
            忽略重复复制
            """
            pass


class HistoryUtil(object):
    cache_record_list = []

    @classmethod
    def batch_get_records(cls, start_pos=0, number=10):
        """
        start_pos : 起始位置
        number : 读几条
        """
        records = []
        with open(get_base_conf_obj().history_file_path, 'r') as f:
            record = ''
            cur_pos = 0
            lines = f.readlines()
            lines.reverse()
            for buffer in lines:
                if buffer != base_spilter:
                    record = buffer + record
                else:
                    # 如果是分隔符，pos += 1；
                    cur_pos += 1
                    # 忽略结尾的 base_spilter
                    if cur_pos == 1:
                        continue
                    records.append(record)
                    # 清空 buffer
                    record = ''
                    if cur_pos > number:
                        break
        return [str(rec + 1) + ' ' + records[rec] for rec in range(0, len(records))]
