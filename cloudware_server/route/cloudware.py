from cloudware_server.route.base import BasicRoute
from cloudware_server.common.role import RoleBuilder


class PostItemRoute(BasicRoute):
    """
    同步数据到服务器
    """
    methods = ['POST']

    def rule_name(self):
        return 'history/item'

    def process(self):
        return "suc"

    def roles(self):
        # 只有用户才能访问
        return RoleBuilder().append_user().build()


class GetItemRoute(BasicRoute):
    """
    从服务器拉数据
    """
    methods = ['GET']

    def rule_name(self):
        return 'history/item'

    def process(self, content=None, content_type=None):
        return super().process()

    def roles(self):
        return RoleBuilder().append_user().build()
