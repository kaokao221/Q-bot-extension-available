import Manager


class Info(Manager.Info):
    def __init__(self) -> None:
        super().__init__(
            Name="关于",
            Description="显示关于信息",
            Writer="admin",
            Version="0"
        )


class Events:
    def __init__(self) -> None:
        self.Events = [
            Manager.events.NewGroupInvited(),
        ]

    @staticmethod
    def when_fetch_new_message():
        if Manager.NewMessageFetched.export_to(str) in [
            "/about",
            "/about@" + Manager.NewMessageFetched.Group.BotName,
            ".about",
            "qbea://panel/about",
            "qbea://about/",
            "qbea://panel/about/",
            "qbea://about"
        ]:
            Manager.Message.new("关于机器人：\n"
                                "版本 alpha:02\n"
                                "作者: kaokao221\n"
                                "项目页面: https://github.com/kaokao221/Q-bot-extension-available/").sendto(
                Manager.NewMessageFetched.Group
            )
