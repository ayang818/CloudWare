from cloudware_client_py.core.target.base_target import BaseTarget


import pyperclip

class ClipBoardTarget(BaseTarget):

    def fetch_one(self):
        return pyperclip.paste()
