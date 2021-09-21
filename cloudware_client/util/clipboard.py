import logging
import os

import requests
from cloudware_client.conf.conf import get_base_conf_obj, remote_server
from cloudware_client.util.account import AccountUtil
from cloudware_client.util.encrypt import EncryptUtil
import time

base_spliter = "|.#.#.#.#.|\n"


class ClipboardUtil(object):
    cache_record_list = []
    # 本地历史纪录 id
    # TODO 持久化，重启不失效
    local_tag_seq_id = ""

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
        user_id = AccountUtil.get_user_id()
        secret_text = ""
        # 目前只支持 text
        if content_type == 'text':
            secret_text = EncryptUtil.encrypt(content, AccountUtil.get_secret_key())
            if not secret_text:
                logging.error("加密失败")
                return
            # if success : update local_tag_seq
        device_id = AccountUtil.get_device_id()
        seq_id = cls.get_tag_seq_id()
        params = {
            "user_id": user_id,
            "secret_text": secret_text,
            "device_id": device_id,
            "tag_seq": seq_id
        }
        #  将当前这条纪录更新到远端
        resp = requests.post(remote_server + "history/post_item", json=params)
        if resp.status_code == 200:
            # 同步更新本地 seq
            cls.local_tag_seq_id = seq_id
            logging.info("成功更新到远端；cur seq=%s", cls.local_tag_seq_id)

    @classmethod
    def sync_from_remote(cls):
        user_id = AccountUtil.get_user_id()
        current_seq_id = cls.local_tag_seq_id
        if not current_seq_id:
            # 如果没有，那就使用当前时间，不对历史纪录做获取
            current_seq_id = cls.get_tag_seq_id()
        # 从 remote_cloudware 获取 所有 大于 current_seq_id 的 history； return []
        params = {
            "user_id": user_id,
            "seq_id": current_seq_id
        }
        resp = requests.get(remote_server + "history/get_item", params=params)
        if resp.status_code == 200:
            # 回刷纪录
            logging.info("成功回刷纪录，cur seq=%s", cls.local_tag_seq_id)

    @classmethod
    def get_tag_seq_id(cls):
        # TODO
        #  暂时用毫秒级时间戳来表示 tag_seq_id
        return int(round(time.time() * 1000))


if __name__ == '__main__':
    ClipboardUtil.sync_to_remote("loveu jjl", "text")
    # ClipboardUtil.sync_from_remote()
