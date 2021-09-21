import hashlib
from cloudware_client.conf.conf import get_base_conf_obj


class AccountUtil(object):
    salt = "cloudwarelovebytedance"
    user_id = None
    device_id = None
    secret_key = None

    @classmethod
    def get_user_id(cls):
        if not cls.user_id:
            secret_key = get_base_conf_obj().secret_key
            cls.user_id = hashlib.md5((secret_key + cls.salt).encode("utf-8")).hexdigest()
        return cls.user_id

    @classmethod
    def get_device_id(cls):
        if not cls.device_id:
            cls.device_id = get_base_conf_obj().device_id
        return cls.device_id

    @classmethod
    def get_secret_key(cls):
        if not cls.secret_key:
            cls.secret_key = get_base_conf_obj().secret_key
        return cls.secret_key

