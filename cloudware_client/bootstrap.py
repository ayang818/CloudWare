import os
import sys

sys.path.insert(0, os.path.join(__file__, "..\\.."))

import logging
from cloudware_client.const.strategy import sys_2_feature_dict, feature_discription


def get_sys():
    return sys.platform


def config_logger():
    """
    设置日志等级
    """
    logging.getLogger().setLevel(logging.INFO)


config_logger()


def start():
    system = get_sys()
    features = sys_2_feature_dict.get(system)
    if len(sys.argv) == 1:
        # 没传参数
        tips = """
欢迎使用 Cloudware\n
你的命令有\n
        """
        for k, v in features.items():
            tips += "%s   %s\n" % (k, feature_discription.get(k))
        print(tips)
        exit(0)
    if not features:
        logging.error("暂时不支持 %s 系统", system)
        exit(0)
    features.get(sys.argv[1]).start_listen()


if __name__ == '__main__':
    start()