#import os
from os import getcwd, getenv
import sys

curr_dir = getcwd()
print(curr_dir)
# Underlying OS
print(sys.platform)
# Python version
print(sys.version)
# Environment variables
print(getenv('PATH'))
print(sys.executable)