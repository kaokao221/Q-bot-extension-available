import sys

import log
import QuickValues as qv

import random

logger = log.Logger()

if __name__ == "__main__":
    print("Use launch.py instead of this.")
    print("If you run this script more than 1 times in a moment, it will redirect to launch.py.")
    logger.log(", ".join([str(i) for i in range(11, random.randint(12, 99))]), qv.Log.debug)
