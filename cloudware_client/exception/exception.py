from cloudware_client.exception.code import ErrorCode


class SolarException(Exception):
    def __init__(self, code=ErrorCode.UNKNOWN, msg=""):
        self.code = code
        self.msg = msg
    
    def get_code(self):
        return self.code

    def get_msg(self):
        return self.msg
