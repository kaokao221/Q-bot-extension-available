# 这是供脚本([`Script`](/script/))开发者参阅的脚本API指南

Language Switcher
Language | Status | Link
:-: | :-: | :-:
Chinese | ✔ | Here
English | ❌ | Ready

需要注意的是，所有的机器人脚本均写为`Python`脚本，除使用`Manager`API外，与正常开发无异。开发过程中应该极力避免包括但不限于`threading`、`asyncio`等异步与多线程方法，这可能导致意料之外的问题。

## 脚本结构

正常的脚本应该包括四个类（详见[`example_script.py`](/script/example_script.py)）：[`Info`](#info类)、[`Events`](#Events类)、`UnexpectedSituations`和`Configurations`，以下将详细说明四个类的撰写和API方法。

需要注意的是，脚本头部需要先引用模块`Manager`，如下：
```python
import Manager
```

### `Info`类
`Info`是该脚本的基本信息。

这是一个`Info`示例片段
```python
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
`Events`声明了在发生事件时的行为。

这是一个`Events`实力片段

## `Manager`模块
`Manager`是整个`Q-bot-extension-available`(下文简称`QBEA`)中的连接核心，用于简化脚本开发，优化插件结构和连接