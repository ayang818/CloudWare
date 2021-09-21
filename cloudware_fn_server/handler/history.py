import logging

from handler.base_handler import BaseHandler


class PostItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        logging.info("params is %s", params)
        return "suc call post item; params=%s" % params


class GetItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        logging.info("params is %s", params)
        return "suc call get item; params=%s" % params
