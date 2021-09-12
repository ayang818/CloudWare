from cloudware_gui.util import log
from cloudware_gui.util.util import unmarshal_json, marshal_obj
import os
import json
import uuid

base_dir = "~/.cloudware/"
base_conf_file_name = 'conf.json'


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
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    base_conf_file = os.path.join(base_dir, base_conf_file_name)
    if not os.path.exists(base_conf_file):
        with open(base_conf_file, "w") as bf:
            json_text = marshal_obj(CloudWareConf())
            json_dict = json.loads(json_text)
            # 初始化客户端私钥, 直接使用 uuid 即可
            # TODO 密钥是否需要带上 用户信息
            json_dict.set('secret_key', uuid.uuid4().hex)
            json_text = json.dumps(json_dict)
            bf.write(json_text)


if __name__ == '__main__':
    print(unmarshal_json('{"secret_key": "hellojjl"}', CloudWareConf).__dict__)
    print(marshal_obj(CloudWareConf()))
