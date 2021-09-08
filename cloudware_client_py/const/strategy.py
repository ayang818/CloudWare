from cloudware_client_py.core.target.clipboard_target import ClipBoardTarget
from cloudware_client_py.core.sidecar.clipboard_sidecar import ClipBoardSideCar

darwin_2_feature = {
    "cp": ClipBoardSideCar(target=ClipBoardTarget()) 
}

win32_2_feature = {
    "cp": ClipBoardSideCar(target=ClipBoardTarget())
}

sys_2_featuredict = {
    "darwin": darwin_2_feature,
    "win32": win32_2_feature
}


