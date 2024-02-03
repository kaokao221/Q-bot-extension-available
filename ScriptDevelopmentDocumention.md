# 这是供插件开发者参阅的插件API

需要注意的是，所有的插件均写为`Python`脚本，除使用`Manager`API外，与正常开发无异。开发过程中应该极力避免包括但不限于`threading`、`asyncio`等异步与多线程方法，这可能导致意料之外的问题。

## 插件结构

正常的插件应该包括四个类（详见[`example_script.py`](/example_script.py)）：[`Info`](#info类)、[`Events`](#Events类)、`UnexpectedSituations`和`Configurations`，以下将详细说明四个类的撰写和API方法。

### `Info`类
`Info`是该插件的基本信息。

这是一个`Info`示例片段
```Python
class Info(Manager.Info):
    def __init__(self) -> None:
        super().__init__(
            Name="刷屏警告",
            Description="为连续发出超过5条消息的人提示刷屏警告",
            Writer="admin",
            Version="1"
        )
```
`Info`不需要额外的自定义信息，详见[`Manager/__init__.py`](/Manager/__init__.py)

### `Events`类
`Events`声明了在发生事件时的行为，