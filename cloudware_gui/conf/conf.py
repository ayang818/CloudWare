from cloudware_gui.util import log
from cloudware_gui.util.util import unmarshal_json, marshal_obj
import os
import json
import uuid
import logging

base_dir = os.path.join(os.path.expanduser('~'), ".cloudware/")
base_conf_file_name = 'conf.json'
conf = None


class CloudWareConf(object):
    secret_key = ""
    # 历史纪录文件路径配置
    history_file_path = base_dir + "history"
    # 历史纪录文件名
    history_file_name = "history"
    # 图片缓存路径配置
    pic_cache_path = base_dir + "pic_history/"
    paste_hot_key = "ALT ALT"


def check_conf_init():
    # 根路径是否存在
    if not os.path.exists(base_dir):
        logging.warning("根路径不存在，创建~")
        os.makedirs(base_dir)
    base_conf_file = os.path.join(base_dir, base_conf_file_name)
    if not os.path.exists(base_conf_file):
        logging.warn("配置文件不存在，初始化~")
        # 写入配置文件
        with open(base_conf_file, "w") as bf:
            json_text = marshal_obj(CloudWareConf())
            json_dict = json.loads(json_text)
            # 初始化客户端私钥, 直接使用 uuid 即可
            # TODO 密钥是否需要带上 用户信息
            json_dict['secret_key'] = uuid.uuid4().hex
            json_text = json.dumps(json_dict)
            bf.write(json_text)
            logging.info("写入配置文件=%s", json_text)
    conf_obj = None
    with open(base_conf_file, 'r') as cf:
        json_data = cf.read()
        conf_obj = unmarshal_json(json_data, CloudWareConf)
    set_base_conf_obj(conf_obj)


def get_base_conf_obj() -> CloudWareConf:
    global conf
    return conf


def set_base_conf_obj(conf_obj):
    global conf
    conf = conf_obj


if __name__ == '__main__':
    print(unmarshal_json('{"secret_key": "hellojjl"}', CloudWareConf).__dict__)
    print(marshal_obj(CloudWareConf()))
