import os

import logger
import BuildInClasses
import QuickValues

import argparse
import requests

_logger = logger.Logger()

launcher_configs = argparse.ArgumentParser()

local = launcher_configs.add_argument_group(
    "local", "Local running QBEA."
)
local.add_argument(
    "-l",
    "--local",
    help="Run at local device.",
    action='store_true'
)
local.add_argument(
    "-alntqq",
    "--attach-to-local-ntqq",
    help="Run at local device and attach to NT QQ.",
    action='store_true'
)

server = launcher_configs.add_argument_group(
    "server", "Server running QBEA."
)
server.add_argument(
    "-s",
    "--server",
    help="Run at server.",
    action='store_true'
)
server.add_argument(
    "-rp",
    "--remote-port",
    type=int,
    help="Remote port on server.",
    default=16383,
    dest='port'
)

remote = launcher_configs.add_argument_group(
    "remote", "Connect to QBEA on server."
)
remote.add_argument(
    "-rc",
    "--remote-connect",
    type=str,
    help="Remote connecting address on server which lunched QBEA.",
    dest='address'
)

args = launcher_configs.parse_args()


class Bot:
    def __init__(self):
        pass

    def start(self):
        pass


def create() -> Bot:
    return Bot()


if __name__ == "__main__":
    print("Don't run this file directly.")
    _logger.log(
        "Run launcher module directly.",
        QuickValues.Log.warning
    )
    exit(0)

print("QBEA Launching")
print("PreLoading......")

try:
    col, lines = os.get_terminal_size()
except OSError:
    print("Run in Terminal but not IDE or others.")
