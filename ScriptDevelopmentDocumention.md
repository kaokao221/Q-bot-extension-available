# 这是供插件开发者参阅的插件API

需要注意的是，所有的插件均写为`Python`脚本，除使用`Manager`API外，与正常开发无异。开发过程中应该极力避免包括但不限于`threading`、`asyncio`等异步与多线程方法，这可能导致意料之外的问题。

## 插件结构

正常的插件应该形如此（详见[example_script.py](example_script.py)）
```Python
"""
#Name: 刷屏警告
#Description: 为连续发出超过5条消息的人提示刷屏警告
#Writer: admin
#Version: 1
"""

import Manager

class Info(Manager.Info):
    def __init__(self, Name, Description, Writer, Version):
        super().__init__(Name, Description, Writer, Version)

```