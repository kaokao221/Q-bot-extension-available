import os
import json


class MIS:
    def __init__(self, path: str | os.path):
        self._path = path

    @property
    def path(self) -> str | os.path:
        return self._path
