import logging


def config_logger():
    """
    设置日志等级
    """
    logging.getLogger().setLevel(logging.INFO)
