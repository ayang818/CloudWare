import sys
import os
sys.path.insert(0, os.path.join(__file__, "..\.."))

import logging
from cloudware_client_py.const.strategy import sys_2_featuredict


def get_sys():
    return sys.platform

def config_logger():
    """
    设置日志等级
    """
    logging.getLogger().setLevel(logging.INFO)
config_logger()

def start():
    logging.info("args=%s", sys.argv)
    system = get_sys()
    features = sys_2_featuredict.get(system)
    if not features:
        logging.error("暂时不支持 %s 系统", system)
        exit(0)
    features.get(sys.argv[1]).start_listen()

if __name__ == '__main__':
    start()