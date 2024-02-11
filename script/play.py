"""
#Name: ？？？
#Description: ？？？？？？
#Writer: ？？？
#Version: ？？？
"""

import Manager


class Info(Manager.Info):
    def __init__(self) -> None:
        super().__init__(
            Name="？？？",
            Description="？？？？？？",
            Writer="？？？",
            Version="？？？"
        )


class Events:
    def __init__(self) -> None:
        self.Events = [
            Manager.events.NewMessageFetched()
        ]

    @staticmethod
    def when_fetch_new_message():
        if Manager.NewMessageFetched.text == "校溯":
            Manager.Message.new("是男娘").sendto(Manager.NewMessageFetched.Group)


class UnexpectedSituations:
    def __init__(self):
        self.UnexpectedSituations = []


if __name__ == '__main__':
    print(Manager.NewMessageFetched)
