from cloudware_client.core.target.clipboard_target import ClipBoardTarget
from cloudware_client.core.sidecar.base_sidecar import BaseSideCar
import logging
from PIL import ImageGrab, Image
import io


class ClipBoardSideCar(BaseSideCar):
    """
    PC跨平台的监听剪贴版事件
    """

    def __init__(self, target: ClipBoardTarget):
        self.target = target
        self.last_content = None

    def process(self):
        content = self.target.fetch_one()
        # 如果为空，可能是图片文件，读出二进制文件
        if not content:
            img = ImageGrab.grabclipboard()
            img_bytes = io.BytesIO()
            if isinstance(img, Image.Image):
                img.save(img_bytes, 'png')
                content = img_bytes.getvalue()
        if content and (not self.last_content or content != self.last_content):
            logging.info("lastest copy=%s", content)
            # 1. save 2 localStorage
            # 2. send 2 remote
            self.last_content = content
        else:
            """
            忽略重复复制
            """
            pass
