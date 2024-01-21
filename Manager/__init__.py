class Info:
    def __init__(self, Name:str, Description:str, Writer:str, Version:str):
        self.Name = Name
        self.Description = Description
        self.Writer = Writer
        self.Version = Version
    
    def __str__(self) -> str:
        return f"插件[{self.Name}]，当前版本号：{self.Version}，由[{self.Writer}]开发。"

