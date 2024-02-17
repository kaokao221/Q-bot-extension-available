import argparse

from message import Message
from events import *
from unexpectedSituations import *


class Info:
    def __init__(self, Name: str, Description: str, Writer: str, Version: str) -> None:
        self._Name = Name
        self._Description = Description
        self._Writer = Writer
        self._Version = Version

    @property
    def Name(self) -> str:
        return self._Name

    @property
    def Description(self) -> str:
        return self._Description

    @property
    def Writer(self) -> str:
        return self._Writer

    @property
    def Version(self) -> str:
        return self._Version

    def __str__(self) -> str:
        return "插件{}，当前版本号：{}，由{}开发。".format(self._Name, self._Version, self._Description)


parser = argparse.ArgumentParser()
parser.add_argument("--process-type", type=str, default="NewMessageFetched")
parser.add_argument("--message-id", type=int, default=-1)
NewMessageFetched = message.Fetch(id=parser.message_id)

if __name__ == "__main__":
    print(parser)
    print(parser.message_id)
