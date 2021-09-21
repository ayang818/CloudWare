# -*- coding: utf-8 -*-
import json
import logging
import os
import sys
from urllib.parse import unquote

sys.path.insert(0, os.path.join(__file__, ".."))
from router import invoke_route

HELLO_WORLD = b'Hello world!\n'


# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
def initializer(context):
    logger = logging.getLogger()
    logger.info('initializing')


def parse_params(body, type):
    params = {}
    if type == 'json':
        try:
            params = json.loads(body)
        except Exception as e:
            logging.error("post 参数解析失败")
    else:
        if body:
            spls = body.split("&")
            for spl in spls:
                if spl:
                    kv = spl.split("=")
                    if len(kv) > 1 and kv[0]:
                        params[kv[0]] = kv[1]
    return params


def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    # 路径
    path = environ.get('PATH_INFO', '/')
    # http method
    req_method = environ['REQUEST_METHOD']
    # 这里统一处理入参为 一个 dict
    if req_method == 'GET':
        params = {}
        params = parse_params(environ['QUERY_STRING'], type='query_str')
        logging.info("get req body=%s", environ['QUERY_STRING'])
    elif req_method == "POST":
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        request_body_str = unquote(environ["wsgi.input"].read(request_body_size).decode('utf-8'))
        logging.info("post req body=%s", request_body_str)
        params = parse_params(request_body_str, type="json")
    else:
        status = '403 FAILED'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ['method not support']
    logging.info("handle req: path=%s; body=%s; method=%s", path, params, req_method)

    # 统一调用路由
    resp = invoke_route(path, params)
    json.dumps(resp)
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    resp = json.dumps(resp)
    logging.info("resp=%s", resp)
    resp = resp.encode("utf-8")
    return [resp]
