import argparse

from message import Message
from events import *
from unexpectedSituations import *


class Info:
    def __init__(self, Name: str, Description: str, Writer: str, Version: str) -> None:
        self.Name = Name
        self.Description = Description
        self.Writer = Writer
        self.Version = Version

    def __str__(self) -> str:
        return "插件{}，当前版本号：{}，由{}开发。".format(self.Name, self.Version, self.Description)


parser = argparse.ArgumentParser()
parser.add_argument("--process-type", type=str, default="NewMessageFetched")
parser.add_argument("--message-id", type=int, default=-1)
NewMessageFetched = message.Fetch(id=parser.message_id)

if __name__ == "__main__":
    print(parser)
    print(parser.message_id)
