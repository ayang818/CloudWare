import json
import logging


def unmarshal_json(json_str, obj):
    """
    解析 json 字符串为 obj
    :param json_str:
    :param obj:
    :return:
    """
    json_dict = {}
    try:
        json_dict = json.loads(json_str.encode("utf-8"))
    except Exception as e:
        print("json cast failed")
        logging.error("json syntax error")
    obj_instance = obj()
    # TODO 按照 ConfObj 为准
    for k, v in json_dict.items():
        setattr(obj_instance, k, v)
    logging.debug("str unmarshal=%s", obj_instance.__dict__)
    return obj_instance


def marshal_obj(obj):
    """
    解析 obj 为 json 字符串
    :param obj:
    :return: str
    """
    json_dict = {}
    for field in dir(obj):
        if field.startswith("__"):
            continue
        val = getattr(obj, field)
        json_dict[field] = val
    json_text = json.dumps(json_dict)
    logging.debug("obj marshal=%s", json_text)
    return json_text
