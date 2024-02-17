import Manager

dirty_keywords = {
    "WarningLevel": ["shit"],
    "BlockLevel": ["fuck"]
}


class Info(Manager.Info):
    def __init__(self) -> None:
        super().__init__(
            Name="脏词过滤",
            Description="脏词过滤",
            Writer="admin",
            Version="1"
        )


class Events:
    def __init__(self) -> None:
        self.Events = [
            Manager.events.NewMessageFetched
        ]

    @staticmethod
    def when_fetch_new_message():
        if True in [result in Manager.NewMessageFetched.text for result in dirty_keywords["WarningLevel"]]:
            Manager.NewMessageFetched.Sender.ChangeName("[警告]" + Manager.NewMessageFetched.Sender.Name, auto_cut=True)

        if True in [result in Manager.NewMessageFetched.text for result in dirty_keywords["BlockLevel"]]:
            Manager.NewMessageFetched.Sender.Block()


class UnexpectedSituations:
    def __init__(self):
        self.UnexpectedSituations = [
            Manager.unexpectedSituations.AdminPermissionNeed
        ]


if __name__ == '__main__':
    print(Manager.NewMessageFetched)
