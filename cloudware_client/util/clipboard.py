import logging
import os

from cloudware_client.conf.conf import get_base_conf_obj

base_spliter = "|.#.#.#.#.|\n"


class ClipboardUtil(object):
    cache_record_list = []
    # 本地历史纪录 tag。fetch
    local_history_record_tag = ""

    @classmethod
    def batch_get_records(cls, start_pos=0, number=100):
        """
        start_pos : 起始位置
        number : 读几条
        """
        records = []
        history_file = get_base_conf_obj().history_file_path
        if not os.path.exists(history_file):
            with open(history_file, 'w') as f:
                logging.info("初始化历史数据文件~")
        with open(history_file, 'r') as f:
            record = ''
            cur_pos = 0
            lines = f.readlines()
            lines.reverse()
            for buffer in lines:
                if buffer != base_spliter:
                    record = buffer + record
                else:
                    # 如果是分隔符，pos += 1；
                    cur_pos += 1
                    # 忽略结尾的 base_spliter
                    if cur_pos == 1:
                        continue
                    records.append(record)
                    # 清空 buffer
                    record = ''
                    if cur_pos > number:
                        break
        return records

    @classmethod
    def get_last_record(cls):
        records = cls.batch_get_records(start_pos=0, number=1)
        return records[0] if len(records) >= 1 else None

    @classmethod
    def sync_to_remote(cls, content, content_type):
        """
        同步一条纪录到远端的 CloudWare
        :param content:
        :param content_type:
        :return:
        """
        pass

    @classmethod
    def sync_from_remote(cls):
        pass
