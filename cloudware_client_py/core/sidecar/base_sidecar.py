from cloudware_client_py.exception.code import ErrorCode
from cloudware_client_py.exception.exception import SolarException
from cloudware_client_py.core.target.base_target import BaseTarget
import time

class BaseSideCar(object):

    def __init__(self, target: BaseTarget):
        self.target = target

    def start_listen(self, interval=1):
        """
        一般以轮询的方式开始监听
        默认轮询间隔 1s
        """
        while True:
            self.process()
            time.sleep(interval)
            
    
    def process(self):
        """
        每次轮询做什么处理
        """
        raise SolarException(code=ErrorCode.METHOD_UNIMPLEMENT, msg="方法未实现")