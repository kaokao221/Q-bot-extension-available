import sys

import logger
import QuickValues

import random

_logger = logger.Logger()

if __name__ == "__main__":
    print("Use launch.py instead of this.")
    print("If you run this scripts more than 1 times in a moment, it will redirect to launch.py.")
    _logger.log(", ".join([str(i) for i in range(11, random.randint(12, 99))]), QuickValues.Log.debug)
