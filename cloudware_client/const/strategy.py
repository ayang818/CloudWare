from cloudware_client.core.target.clipboard_target import ClipBoardTarget
from cloudware_client.core.sidecar.clipboard_sidecar import ClipBoardSideCar

darwin_2_feature = {
    "cp": ClipBoardSideCar(target=ClipBoardTarget())
}

win32_2_feature = {
    "cp": ClipBoardSideCar(target=ClipBoardTarget())
}

sys_2_feature_dict = {
    "darwin": darwin_2_feature,
    "win32": win32_2_feature
}

feature_description = {
    "cp": "剪贴板历史（支持跨设备同步。默认关闭）"
}
