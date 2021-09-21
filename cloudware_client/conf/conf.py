from cloudware_gui.util import log
from cloudware_client.util.json_util import unmarshal_json, marshal_obj
import os
import json
import shortuuid
import logging

base_dir = os.path.join(os.path.expanduser('~'), ".cloudware\\")
base_conf_file_name = 'conf.json'
conf = None


class CloudWareConf(object):
    device_id = ""
    secret_key = ""
    # 历史纪录文件路径配置
    history_file_path = base_dir + "history"
    # 历史纪录文件名
    history_file_name = "history"
    # 图片缓存路径配置
    pic_cache_path = base_dir + "pic_history/"
    paste_hot_key = "ALT ALT"


# TODO 这里很奇怪，应用内运行就能 load 成功，单独启动就不行
def read_conf_from_file(path):
    conf_obj = None
    with open(path, 'r') as cf:
        json_data = cf.read()
        conf_obj = unmarshal_json(json_data, CloudWareConf)
    return conf_obj


def get_base_conf_obj() -> CloudWareConf:
    global conf
    if not conf:
        conf = read_conf_from_file(os.path.join(base_dir, base_conf_file_name))
    return conf


def set_base_conf_obj(conf_obj):
    global conf
    conf = conf_obj


def check_conf_init():
    # 根路径是否存在
    if not os.path.exists(base_dir):
        logging.warning("根路径不存在，创建~")
        os.makedirs(base_dir)
    base_conf_file = os.path.join(base_dir, base_conf_file_name)
    if not os.path.exists(base_conf_file):
        logging.warning("配置文件不存在，初始化~")
        # 写入配置文件
        with open(base_conf_file, "w") as bf:
            json_text = marshal_obj(CloudWareConf())
            json_dict = json.loads(json_text)
            # 初始化客户端私钥, 直接使用 uuid 即可
            # TODO 密钥是否需要带上 用户信息
            json_dict['secret_key'] = shortuuid.ShortUUID().random(length=16)
            json_dict['device_id'] = shortuuid.ShortUUID().random(length=16)
            json_text = json.dumps(json_dict)
            bf.write(json_text)
            logging.info("写入配置文件=%s", json_text)
    conf_obj = None
    conf_obj = read_conf_from_file(base_conf_file)
    set_base_conf_obj(conf_obj)


check_conf_init()

if __name__ == '__main__':
    print(unmarshal_json('{"secret_key": "hellojjl"}', CloudWareConf).__dict__)
    print(marshal_obj(CloudWareConf()))
    print(get_base_conf_obj().__dict__)
    # print(read_conf_from_file("C:\\Users\\cheng\\.cloudware\\conf.json").__dict__)
