import os
import sys

sys.path.insert(0, os.path.join(__file__, "..\\.."))

import logging
from cloudware_client.const.strategy import sys_2_feature_dict, feature_description


def get_sys():
    return sys.platform


def config_logger():
    """
    设置日志等级
    """
    logging.getLogger().setLevel(logging.INFO)


config_logger()


def start(command='cp'):
    system = get_sys()
    features = sys_2_feature_dict.get(system)
    if not command:
        # 没传参数
        tips = """
欢迎使用 Cloudware\n
你的命令有\n
        """
        for k, v in features.items():
            tips += "%s   %s\n" % (k, feature_description.get(k))
        print(tips)
        exit(0)
    if not features:
        logging.error("暂时不支持 %s 系统", system)
        exit(0)
    features.get(command).start_listen(interval=0.5)


if __name__ == '__main__':
    start()
