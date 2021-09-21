from handler.base_handler import BaseHandler


class PostItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        return "suc call post item; params=%s" % params


class GetItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        # 每个 uid 都是由客户端的 md5(secret_key) 得到的
        uid = params
        return "suc call get item; params=%s" % params
