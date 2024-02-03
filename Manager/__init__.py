import argparse
import message


class Info:
    def __init__(self, Name: str, Description: str, Writer: str, Version: str) -> None:
        self.Name = Name
        self.Description = Description
        self.Writer = Writer
        self.Version = Version

    def __str__(self) -> str:
        return f"插件[{self.Name}]，当前版本号：{self.Version}，由[{self.Writer}]开发。"


parser = argparse.ArgumentParser()
parser.add_argument("--process-type", type=str, default="NewMessageFetched")
parser.add_argument("--message-id", type=int, default=-1)
NewMessageFetched = message.Fetch(id=parser.message_id)
