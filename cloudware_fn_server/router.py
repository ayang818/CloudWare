from handler.history import PostItemHandler, GetItemHandler
from utils.util import SolarException, build_result
import traceback

route = {
    '/history/post_item': PostItemHandler,
    '/history/get_item': GetItemHandler,
}


def invoke_route(path, params):
    """
    统一路由调用方法
    TODO 网关统一做限流
    :param path:
    :param params:
    :return: route process resp
    """
    try:
        klass = route.get(path)
        resp = klass.process(params)
        return build_result(body=resp)
    except SolarException as e:
        traceback.print_exc()
        return build_result(exception=e)
    except Exception as e:
        return build_result(exception=SolarException(msg="Internal Server Error"))
