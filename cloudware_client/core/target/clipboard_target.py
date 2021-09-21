from cloudware_client.core.target.base_target import BaseTarget

import pyperclip


class ClipBoardTarget(BaseTarget):

    def fetch_one(self):
        try:
            return pyperclip.paste()
        except pyperclip.PyperclipWindowsException as e:
            return ""

