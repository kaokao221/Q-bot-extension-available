import os
import importlib

import_libs = [
    ["time", "time"]
]

libs = {}

try:
    col = os.get_terminal_size().columns
    line = os.get_terminal_size().lines
except OSError:
    print("May be launched in IDE, not supported Console UI.")

print("\033c\033[1;1HImporting Modules")
for lib_sick, lib in import_libs:
    libs[lib_sick] = importlib.import_module(lib)

print(libs["time"].time())


