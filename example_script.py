"""
#Name: 刷屏警告
#Description: 为连续发出超过5条消息的人提示刷屏警告
#Writer: admin
#Version: 1
"""

import Manager

class Info(Manager.Info):
    def __init__(self, name):
        super(Info, self).__init__(name, )
