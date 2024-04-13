"""
#Name: 刷屏警告
#Description: 为连续发出超过5条消息的人提示刷屏警告
#Writer: admin
#Version: 1
"""

import Manager


class Info(Manager.Info):
    def __init__(self) -> None:
        super().__init__(
            Name="刷屏警告",
            Description="为连续发出超过5条消息的人提示刷屏警告",
            Writer="admin",
            Version="1"
        )


class Events:
    def __init__(self) -> None:
        self.Events = [
            Manager.events.NewGroupInvited(),
            Manager.events.NewMessageFetched()
        ]

    @staticmethod
    def when_invite_new_group():
        Manager.GroupManager.Agree()
        Manager.Message.new("大家好！").sendto(Manager.NewGroptInvited)

    @staticmethod
    def when_fetch_new_message():
        if Manager.NewMessageFetched.offset(1) == Manager.NewMessageFetched.offset(
                2) and Manager.NewMessageFetched.offset(2) == Manager.NewMessageFetched.offset(
                3) and Manager.NewMessageFetched.offset(3) == Manager.NewMessageFetched.offset(
                4) and Manager.NewMessageFetched.offset(4) == Manager.NewMessageFetched:
            Manager.Message.new("[警告]", Manager.NewMessageFetched.sender.at, "刷屏").sendto(
                Manager.NewMessageFetched.Group)
            Manager.GroupManage.ban(Manager.NewMessageFetched.sender)


class UnexpectedSituations:
    def __init__(self):
        self.UnexpectedSituations = [
            Manager.unexpectedSituations.AdminPermissionNeed
        ]


if __name__ == '__main__':
    print(Manager.NewMessageFetched)
