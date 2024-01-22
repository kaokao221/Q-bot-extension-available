class NewMessageFetched:
    def __init__(self) -> None:
        pass

class NewGroupInvited:
    def __init__(self) -> None:
        pass

class UnexpectedEvent(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
