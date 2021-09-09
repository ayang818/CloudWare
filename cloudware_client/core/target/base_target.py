from cloudware_client.exception.code import ErrorCode
from cloudware_client.exception.exception import SolarException


class BaseTarget(object):

    def fetch(self):
        raise SolarException(code=ErrorCode.METHOD_UNIMPLEMENT, msg="方法未实现")

    def fetch_one(self):
        raise SolarException(code=ErrorCode.METHOD_UNIMPLEMENT, msg="方法未实现")
